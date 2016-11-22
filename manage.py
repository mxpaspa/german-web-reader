import os
from germanapp.database import session, Article
from flask.ext.script import Manager
from germanapp import app


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
@manager.command
def seed():
        article = Article(
             "http://www.breitbart.com/national-security/2016/11/09/foreign-leaders-react-donald-trumps-election-victory/"
        )
        session.add(id)
        session.commit()

if __name__ == "__main__":
    manager.run()
    
