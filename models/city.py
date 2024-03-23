#!/usr/bin/python3
""" Module for City class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class"""
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship("Place", backref="cities", cascade="all, delete")
