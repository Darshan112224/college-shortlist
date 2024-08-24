# import sqlite3

import sqlite3


def create_database():
    connection = sqlite3.connect('colleges.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Colleges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        tuition REAL,
        acceptance_rate REAL,
        programs TEXT
    )
    ''')
    
    connection.commit()
    connection.close()

# If you are using SQLAlchemy:
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///colleges.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class College(Base):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    tuition = Column(Float)
    acceptance_rate = Column(Float)
    programs = Column(String)

Base.metadata.create_all(engine)
