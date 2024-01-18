'''All classes that inherit from Base must be imported before calling Base.metadata.create_all(engine)'''
''' a script that lists all State objects from the database hbtn_0e_6_usa
     Your script should connect to a MySQL server running on localhost at port 3306
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the declarative base
Base = declarative_base()

# Define the State classs
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to the MySQL server
engine = create_engine('mysql://user:password@localhost:3306/db_name')
Base.metadata.create_all(engine)
