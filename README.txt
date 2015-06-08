6/7/2015
code written by: Roman Levitas & Udacity team
contact: mrlevitas@yahoo.com

Directions given:
https://docs.google.com/document/d/1jFjlq_f-hJoAZP8dYuo5H3xY62kGyziQmiv9EPIA7tM/pub?embedded=true

***************************Summary**********************************
This zip contains 4 files and 2 folders which combine to build a web
application for a Guitar Catalog using Python, Flask as the framework,
SQLalchemy as the ORM, and a pysqlite database as the back-end to
store data on the guitars to be displayed. User authentication via
Google+ is also implemented to be able to modify the data stored
in the db by a user.

The files and folders are:
1) application.py
2) database_setup.py
3) lotsofguitars.py
4) client_secrets.json
5) ./templates
6) ./static

***************************General Usage****************************
An installation of Python 2.7 is required to run the web application.

To run the Guitar Catalog Web App project:

1. Install Git, Virtualbox to run a VM, and Vagrant to configure 
   and manage it.
   Instructions can be found here:
   https://www.udacity.com/wiki/ud197/install-vagrant

   This allows us to run the webapp from a VM where the ports have
   been forwarded and the application can run locally on localhost.

2. Make sure the cloned repository is located where vagrant recognizes
   the shared folder between your VM and local machine

3. Login to vagrant using 'vagrant up' & 'vagrant ssh' and navigate 
   to the directory inside the vagrant environment which contains 
   the 'catalog' folder

4. run database_setup.py to create the database

5. run lotsofguitars.py to populate the database

6. run application.py and navigate to localhost:5000 in your browser

*******************************files & folders*******************************

1) application.py
################################################################################
This is the main file of the application which binds to the db and associates 
all of the different url routes available to methods using decorators. It links
each method to its designated HTML template for rendering and parses the url 
for parameters.

It also implements user authentication via Google+.

 
2) database_setup.py
################################################################################
This file is used to set up the database used to store the different guitar 
types available in the catalog as well as specific guitar models each of which
occupy their own table. A user table is also created to keep track of who has
logged into the application.

guitarType associates itself with a unique id, their name, and a user id.

guitarInfo associates itself with a specific guitar model, including its 
unique id, name, price, description, number of strings, and again user id.

3) lotsofguitars.py
################################################################################
This file executes manual inserts into the db of different guitar types as well
as specific models for each type. Data is cited from www.guitarcenter.com

4) client_secrets.json
################################################################################
File contains 'secret' necessary for getting tokens from google api.

5) ./templates
################################################################################
Folder contains all the HTML templates necessary for rendering all available 
urls in web application.

6) ./static
################################################################################
Folder contains css file for styling HTML templates.
