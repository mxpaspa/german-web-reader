import os
from database import session, Article
from flask.ext.script import Manager
from runserver import app


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def seed():
        urls = [
                "https://www.welt.de/kultur/kunst-und-architektur/article162781863/Deutsche-Mediziner-loesen-Raetsel-um-Mona-Lisas-Laecheln.html"
               ]
        for url in urls:
            article = Article()
            article.url = url
            session.add(article)
            session.commit()

if __name__ == "__main__":
    manager.run()
