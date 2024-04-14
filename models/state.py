#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        name = ''

        @property
        def cities(self):
            '''
            returs llist of cities
            '''
            from models import storage
            from models.city import City
            cities = []
            state_id = self.id
            for k, v in storage.all(City).items():
                if v.state_id == state_id:
                    cities.append(v)
            else:
                return cities
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship('City', back_populates='state')
