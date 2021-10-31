from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Question(Base):
  __tablename__ = 'question'
  table_id = Column(Integer, primary_key = True)
  username = Column(String)
  text = Column(String)