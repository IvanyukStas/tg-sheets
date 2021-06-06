from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///foo.db')
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=db)
session = Session()