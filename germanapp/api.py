from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session, Article
from flask import flash


@app.route("/")
def front_page():
    return render_template("german.html")

@app.route("/api/display_content/")
def display_first():
    article = session.query(Article).first()
    return render_template("iframe.html", article = article)
    
@app.route("/api/display_content/<id>")
def display_content(id):
    article = session.query(Article).filter_by(id = id).all()
    return render_template("iframe.html", article = article)

@app.route("/api/previous_article/<id>")
def display_previous(id):
    current = []
        
    current = list(Article.id('id', 'url', flat=True)).index(id)
    article = session.query(Article).index(current-1)
    return render_template("iframe.html", article = article)
   