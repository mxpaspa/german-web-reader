from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

from . import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Article(Base):
    __tablename__ = "articles"
    
    url = Column(String, primary_key=True)

Base.metadata.create_all(engine)
