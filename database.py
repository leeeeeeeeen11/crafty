from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_question(username,text):
  new_question = Question(username = username, #creates a q object
                          text = text)
  session.add(new_question) #opens the db and puts the new q
  session.commit() #closes the db


def get_all():
   qs = session.query(
      Question).all()
   return qs


