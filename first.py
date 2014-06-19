from flask import Flask
from database import db_session
from models import User


app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def hello():
    u = User.query.filter(User.name == 'Shea').first()
    return "%s %s" % (u.name, u.email)

if __name__ == "__main__":
    app.run()
