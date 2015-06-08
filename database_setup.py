# configuration code GREEN
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# class definition PURPLE
class guitarType(Base):
    # table info YELLOW
    __tablename__ = 'guitar_type'

    # mapper PINK
    id = Column(Integer, primary_key=True)
    # electric guitar, acoustic guitar, left-handed guitar, ukulele
    # electric bass guitar, acoustic bass guitar, upright bass guitar
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


# class definition PURPLE
class guitarInfo(Base):
    # table info YELLOW
    __tablename__ = 'guitar_info'

    # mapper PINK
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    stringNum = Column(Integer)
    type_id = Column(Integer, ForeignKey('guitar_type.id'))
    typeOfGuitar = relationship(guitarType)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):
        return {
           'name': self.name,
           'description': self.description,
           'id': self.id,
           'price': self.price,
            }


# configuration code GREEN
engine = create_engine('sqlite:///guitarCatalogwithusers.db')
Base.metadata.create_all(engine)
