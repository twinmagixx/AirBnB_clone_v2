#!/usr/bin/python3
"""This is the user class"""
import sqlalchemy

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        __tablename__: table name in MySQL
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    reviews = relationship("Review", cascade="all, delete", backref="user")
    places = relationship("Place", cascade="all, delete", backref="user")
