from flask import Flask, render_template, url_for, request, redirect, flash
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, guitarType, guitarInfo, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import time

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Guitar Catalog Application"

engine = create_engine('sqlite:///guitarCatalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# route to login page with google+ authorization
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

# see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
            user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: '
    output += '150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session.get('credentials')
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("You have successfully logged out.")
        return redirect('/')
    else:
        # For whatever reason, the given token was invalid.
        # clear cookies in browser if this error persists
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# API endpoint for all guitar of particular type returned as JSON
@app.route('/guitars/<int:guitar_id>/JSON/')
def guitarTypeJSON(guitar_id):
    items = session.query(guitarInfo).filter_by(type_id=guitar_id).all()
    return jsonify(GuitarItems=[i.serialize for i in items])


# API endpoint for particular guitar returned as JSON
@app.route('/guitars/<int:guitar_id>/<int:specificguitar_id>/JSON/')
def guitarSpecificJSON(guitar_id, specificguitar_id):
    item = session.query(guitarInfo).filter_by(
        type_id=guitar_id, id=specificguitar_id).one()
    return jsonify(GuitarItem=[item.serialize])


# home page
@app.route('/')
@app.route('/guitars/')
def guitarHome():
    allguitarTypes = session.query(guitarType).all()
    if 'username' not in login_session:
        return render_template('publicguitarmain.html',
                               guitars=allguitarTypes)
    return render_template('guitarmain.html', guitars=allguitarTypes)


@app.route('/guitars/<int:guitar_id>/')
def specificguitarListing(guitar_id):
    guitar = session.query(guitarType).filter_by(id=guitar_id).one()
    creator = getUserInfo(guitar.user_id)
    items = session.query(guitarInfo).filter_by(type_id=guitar.id).all()
    if 'username' not in login_session:
        return render_template('publicspecificguitar.html', guitar=guitar,
                               items=items, creator=creator)
    else:
        return render_template(
            'specificguitar.html', guitar=guitar, items=items)


# route for newGuitar function
@app.route('/guitars/<int:guitar_id>/new/', methods=['GET', 'POST'])
def newGuitar(guitar_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newItem = guitarInfo(
            name=request.form['name'], price=request.form['price'],
            description=request.form['description'], type_id=guitar_id,
            user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash("new item %s created!" % newItem.name)
        return redirect(url_for('specificguitarListing', guitar_id=guitar_id))
    else:
        return render_template('newguitaritem.html',  guitar_id=guitar_id)


# Croute for editGuitarItem function
@app.route('/guitars/<int:guitar_id>/<int:specificguitar_id>/edit/',
           methods=['GET', 'POST'])
def editGuitarItem(guitar_id, specificguitar_id):
    if 'username' not in login_session:
        return redirect('/login')
    editItem = session.query(guitarInfo).filter_by(id=specificguitar_id).one()
    if editItem.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this guitar. Please create your own guitar in order to edit.');}</script><body onload='myFunction()''>"

    prevName = editItem.name
    if request.method == 'POST':
        if editItem != []:
            print "inside POST edit"
            editItem.name = request.form['name']
            editItem.price = request.form['price']
            editItem.description = request.form['description']
            session.add(editItem)
            session.commit()
            flash("menu item %s edited and changed to %s!" %
                  (prevName, editItem.name))

        return redirect(url_for('specificguitarListing', guitar_id=guitar_id))
    else:
        return render_template(
            'editguitaritem.html', guitar_id=guitar_id,
            specificguitar_id=specificguitar_id, item=editItem)


# route for deleteGuitarItem function
@app.route('/guitars/<int:guitar_id>/<int:specificguitar_id>/delete/',
           methods=['GET', 'POST'])
def deleteGuitarItem(guitar_id, specificguitar_id):
    if 'username' not in login_session:
        return redirect('/login')

    deleteItem = session.query(guitarInfo).filter_by(id=specificguitar_id).one()
    if deleteItem.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this guitar. Please create your own guitar in order to delete.');}</script><body onload='myFunction()''>"

    if request.method == 'POST':
        if deleteItem != []:
            session.delete(deleteItem)
            session.commit()
            flash("%s deleted!" % deleteItem.name)

        return redirect(url_for('specificguitarListing', guitar_id=guitar_id))

    else:
        return render_template(
            'deleteguitaritem.html', guitar_id=guitar_id, item=deleteItem)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
