from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, DateTime

#User table for database    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)

#Login table info for database model
class UserLogin(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)