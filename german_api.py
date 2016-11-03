from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session, Entry
from flask import flash



@app.route("/api/display_article")
def display_content:
    article = session.query.filter_by(id = id)
    return render_template("iframe.html", article)




    
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




    
    
    
    
   