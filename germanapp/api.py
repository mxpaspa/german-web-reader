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
    
@app.route("/api/display_next/<int:id>")
def display_next(id):
    article_id= session.query(Article).filter_by(id = id).all()
    article_id = [ ]
    next_article = [id[article_id.index(id) + 1] for id in article_id]
    previous_article = [id[article_id.index(id) - 1] for id in article_id]
    return render_template("iframe.html", next_article=next_article, previous_article=previous_article)


   