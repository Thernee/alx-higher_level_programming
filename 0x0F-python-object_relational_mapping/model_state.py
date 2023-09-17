#!/usr/bin/python3

"""Module declaration for model_state."""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base


class State(Base):
    """Class declaration for State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
