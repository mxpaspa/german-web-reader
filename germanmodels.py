import feedparser

###can postgres store URLs?##

class Feed(Base):
    __tablename__ = "feeds"

    newsurls = {
        'apnews':           'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a76b4ad082fe88aa0db04909',
        'googlenews':       'http://news.google.com/?output=rss',
        'yahoonews':        'http://news.yahoo.com/rss/'
    }
    id = Column(Integer, primary_key=True)
    d = feedparser.parse('http://www.reddit.com/r/python/.rss')
    
    def as_dictionary(self):
        file = session.query(File).filter_by(id =self.song_file_id).first()
        
       