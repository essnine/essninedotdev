from flask import (
    Flask,
    current_app,
    g,
    redirect,
    request,
    make_response,
    render_template,
    blueprints,
)

import db
import flask_login
import logging
import os


app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

logger = logging.getLogger(__name__)
login_manager = flask_login.LoginManager()


@app.teardown_appcontext
def close_connection(Exception):
    (str(Exception))
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.get("/blog/{post_id}")
def get_post(post_id):
    post = db.get_single_post(post_id)
    return render_template(post)


@app.route("/blog")
def serve_posts():
    return db.get_all_posts()


@app.get("/")
def index():
    posts = db.get_all_posts()
    response = render_template("index.html")
    return response


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return {}


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    Flask.run(app, debug=True)
