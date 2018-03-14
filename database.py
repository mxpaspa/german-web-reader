from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

# from . import app


#from api import app
# from runserver import app


#engine = create_engine(app.config["DATABASE_URI"])
#engine = create_engine("postgresql://ubuntu:thinkful@localhost:5432/germanapp")
engine = create_engine("postgresql://localhost:5432/germanapp")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Article(Base):
    __tablename__ = "articles"

    url = Column(String, nullable=False)
    id = Column(Integer, primary_key=True)

Base.metadata.create_all(engine)
