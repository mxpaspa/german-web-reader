from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session, Article
from flask import flash

global article
global next_article

@app.route("/")
def front_page():
    return render_template("german.html")

@app.route("/api/display_content/")
def display_first():
    article = session.query(Article).first()
    return render_template("iframe.html", article = article)

@app.route("/api/display_next/<id>/")
def display_next(id):
    next_article = session.query(Article).filter_by(id = id).next(article.id)
def display_previous(id):
    previous_article = session.query(Article).filter_by(id = id).get(next_article.id - 1)
    return render_template("iframe.html", next_article = next_article, previous_article = previous_article)
    



   