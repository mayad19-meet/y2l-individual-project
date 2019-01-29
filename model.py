from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :



# Place your database schema code here

# Example code:
class Account(Base):
    __tablename__ = "accounts"
    id=Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username=Column(String, unique=True)   
    password= Column(String)
    
   
    def __repr__(self):
        return ("first_name: {}, last_name: {},Username: {}, Password: {}".format(self.first_name,self.last_name,self.username, self.password))

