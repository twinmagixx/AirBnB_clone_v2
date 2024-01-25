#!/usr/bin/python3
"""This is the city class"""
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: column for state id (foreign key)
        name: column for name of city
        __tablename__: name of table in MySQL
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities")
