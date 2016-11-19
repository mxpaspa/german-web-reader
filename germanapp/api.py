from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session, Article
from flask import flash



@app.route("/api/display_article/{id}")
def display_content():
    article = session.query.filter_by(id = id)
    return render_template("iframe.html", article = article)




    




    
    
    
    
   