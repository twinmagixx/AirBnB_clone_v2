#!/usr/bin/python3
"""This is the state class"""

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if ('HBNB_TYPE_STORAGE' not in environ or
            environ['HBNB_TYPE_STORAGE'] != 'db'):
        """Conditional getters and setters for review and amenities
            Only executed when file storage is being used
        """
        @property
        def cities(self):
            """Returns the list of City instances with equal state_id"""
            from models import storage
            cities = storage.all(City)
            self.__cities = [city for city in cities.values()
                             if city.state_id == self.id]
            return self.__cities
