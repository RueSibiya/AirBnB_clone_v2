#!/usr/bin/python3
""" This module defines the User class, inherits from BaseModel """

import uuid
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """A user class that inherits from BaseModel and Base"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new User"""
        super().__init__(*args, **kwargs)
