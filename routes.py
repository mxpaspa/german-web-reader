from flask import render_template, Flask
from flask import request, redirect, url_for
# from germanapp import app
from database import session, Article
# from flask import flash

global article

#app = Flask(__name__)
from runserver import app

@app.route("/")
def front_page():
    return render_template("german.html")

@app.route("/api/display_content/<id>")
def display_content(id = 1):

    article = session.query(Article).filter(Article.id == id).first()


    print("article: ")
    print(article)

    next_article = get_next(article.id)
    previous_article = get_previous(article.id)
    return render_template("iframe.html", article = article, next_article=next_article, previous_article=previous_article)

def get_next(id):
    next_article = session.query(Article).filter(Article.id > id).first()
    return next_article

def get_previous(id):
    previous_article = session.query(Article).filter(Article.id < id).first()
    return previous_article

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
