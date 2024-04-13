#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
=======
from sqlalchemy import Column, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
>>>>>>> 9d8f76340052d4583dad0a15bfc3d6c5a75db260

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
