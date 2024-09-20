'''
1. create engine
2.create session( from .orm)
3.create table (declarative base from ext.declarative)
4.migrate
'''
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
engine = create_engine('postgresql://postgres:pass@localhost:5432/sql_alchemy_learning')

Session = sessionmaker(bind=engine)
Session= Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine)