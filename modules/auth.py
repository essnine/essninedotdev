import functools
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import generate_password_hash

from db import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = db.auth_user(
            username=username, password_hash=generate_password_hash(password)
        )
        if not user:
            return "username or password is wrong", 404
    return {}
