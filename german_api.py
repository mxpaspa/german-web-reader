




newsurls = {
    'apnews':           'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a76b4ad082fe88aa0db04909',
    'googlenews':       'http://news.google.com/?output=rss',
    'yahoonews':        'http://news.yahoo.com/rss/'
}


@app.route("/api/feeds", methods=["GET"])
@decorators.accept("application/json")
def parse_RSS( rss_url):
    """ Get articles through next article """
    return feedparser.parse( rss_url ) 


def parse_feed_content( rss_url)
for urls in Feed:
    Feed.parse_RSS()





    
@app.route("/api/feed_content", methods=["GET"])
@decorators.accept("application/json")
def parse_RSS( rss_url):
    """ Get articles through next article """
    def getContent( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        hea
    
    return headlines
    
    
    
    
    
    
   