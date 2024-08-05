import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    registration_date = Column(String(20), nullable=False)
    susbcription_date = Column(String(20), nullable=False)
    subscription_status = Column(String(20), nullable=False)
    user_status = Column(String(20), nullable=False)

class UserCredentials(Base):
    __tablename__ = 'user_credentials'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    password = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Float)
    orbital_period = Column(Float)
    gravity = Column(String(10))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(50))
    surface_water = Column(Float)
    created = Column(String(50))
    edited = Column(String(50))
    name = Column(String(50))
    url = Column(String(100))
    description = Column(String(200))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(50))
    gender = Column(String(10))
    created = Column(String(50))
    edited = Column(String(50))
    name = Column(String(50))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    url = Column(String(100))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
