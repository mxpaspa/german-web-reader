import feedparser

###can postgres store URLs?##

class Feed(Base):
    __tablename__ = "selected_feeds"

    newsurls = {
        'apnews':           'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a76b4ad082fe88aa0db04909',
        'googlenews':       'http://news.google.com/?output=rss',
        'yahoonews':        'http://news.yahoo.com/rss/'
    }
    id = Column(Integer, primary_key=True)
    
    
    
       