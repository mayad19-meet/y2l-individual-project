from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    pass


# Place your database schema code here

# Example code:
class Account(Base):
    __tablename__ = "accounts"
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, primary_key = True)
    
    password= Column(String)
    
   
    def __repr__(self):
        return ("first_name: {}, last_name: {},Username: {}, Password: {}"
        .format(self.first_name,self.last_name,self.username, self.password))

# class Post(Base):
#     __tablename__="posts"
#     post_id= Column(Integer, primary_key =True)
#     title=Column(String)
#     content= Column(String)
#     picture= Column(String)
#     username = Column(String, ForeignKey('accounts.username'))
#     user = relationship("Account", back_populates="posts")

    # def __repr__(self):
    #     return("Title: {}, Content: {}.ID: {}".format(self.title,self.content,self.post_id))