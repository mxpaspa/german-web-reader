from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session, Article
from flask import flash


@app.route("/")
def front_page():
    return render_template("german.html")
    
@app.route("/api/display_content/")
def display_content(article):
    articles = session.query(Article).filter_by(iarticle = article)
    return render_template("iframe.html", articles = articles)


    




    
    
    
    
   