from flask import g, current_app
import sqlite3
import os

DATABASE = os.getenv("DB_PATH", "data.db")

"""
--- POSTS_SCHEMA ---
ID, TITLE, CONTENT, CREATED, TAGS, ACTIVE
"""

FETCH_ALL_POSTS_QUERY = (
    "SELECT ID, TITLE, CREATED, TAGS FROM POSTS WHERE ACTIVE = 1 ORDER BY CREATED DESC;"
)
FETCH_POST_BY_ID_QUERY = (
    "SELECT * FROM POSTS WHERE ID = ? AND ACTIVE = 1 SORT BY CREATED DESC;"
)
DELETE_POST_SOFTLY = "UPDATE POSTS SET ACTIVE = 0 WHERE ID = ?;"


def get_db() -> sqlite3.Connection:
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_posts():
    db = get_db()
    posts_cur = db.cursor().execute(FETCH_ALL_POSTS_QUERY)
    posts_list = posts_cur.fetchall()
    return posts_list


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    if os.path.exists("DATABASE"):
        return

    with current_app.open_resource("schema.sql") as f:
        db_script = str(f.read().decode("utf8"))
        db.executescript(db_script)


def get_single_post(post_id):
    db = get_db()
    query_params = (post_id,)
    posts_cur = db.cursor().execute(FETCH_POST_BY_ID_QUERY, query_params)
    posts_list = list(posts_cur.fetchone())
    return posts_list


def delete_single_post(post_id):
    db = get_db()
    query_params = (post_id,)
    posts_cur = db.cursor().execute(DELETE_POST_SOFTLY, query_params)
    posts_list = posts_cur.fetchone()
    return posts_list
