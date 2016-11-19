import feedparser

###can postgres store URLs?##

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)

Base.metadata.create_all(engine)

    
       