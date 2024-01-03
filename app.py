from flask import Flask, current_app, g, request, make_response, render_template
import db
import logging


app = Flask(
    __name__,
)
logger = logging.getLogger(__name__)

with app.app_context():
    db.init_db()


@app.teardown_appcontext
def close_connection(Exception):
    (str(Exception))
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/posts")
def serve_posts():
    return db.get_posts()


@app.get("/")
def index():
    response = render_template("index.html")
    return response


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    Flask.run(app, debug=True)
