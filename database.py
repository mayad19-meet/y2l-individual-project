from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#def function(parameter):
 #   pass
def add_account(first_name,last_name,username,password):           
    print("Added an account")
    account = Account(first_name=first_name,last_name=last_name,username=username,password=password)       
    session.add(account)
    session.commit()

def get_all_users():
    accounts= session.query(Account).all()        
    return accounts
def check_user_exists(username):

    account = session.query(Account).filter_by(username=username).first()
    if account==None:

        return False
    else:
        return True


def check_user_and_pass(username, password):
    print("hello")
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Account).filter_by(username=username,password=password)
    print("check")
    result = query.first()
    if result is not None:
        return True
    else:
       print('wrong password!')
       return False
       
# def get_posts():
#     posts = session.query(Post).all()
#     print(type(posts))
#     posts=reversed(posts)
#     return posts
    
# def add_post(title,content,picture,username):
#    add_post=Post(
#        title=title,
#        content=content,
#        picture=picture,
#        username=username

#    )
 #   session.add(add_post)
#   session.commit()
