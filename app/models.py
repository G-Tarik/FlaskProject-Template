from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    age = Column(Integer)

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<User {}>'.format(self.name)
