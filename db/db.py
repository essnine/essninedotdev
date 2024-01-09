from typing import Any
from flask import g, current_app
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update
from sqlalchemy.exc import NoResultFound

from .models import User, Post

import sqlite3
import os

DB_DSN = os.getenv("DB_DSN")
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite://")
engine = create_engine(DATABASE_URI, echo=False)

"""
--- POSTS_SCHEMA ---
ID, TITLE, CONTENT, CREATED, TAGS, ACTIVE
"""


def register_user(username, password_hash, fullname=None):
    session = Session(engine)
    try:
        user_obj = User(name=username, password=password_hash)
        session.add(user_obj)
        session.commit()
    except Exception as exc:
        current_app.logger.exception("Could not create user: {}".format(str(exc)))
    finally:
        session.close()
    pass


def auth_user(username, password_hash):
    session = Session(engine)
    try:
        find_user_stmt = select(User).where(
            User.name == username, User.password == password_hash
        )
        user = session.scalars(find_user_stmt).one()
    except NoResultFound:
        current_app.logger.info("User: {} not found".format(username))
        return {}
    except Exception as exc:
        current_app.logger.exception("User not found")
        raise exc


def get_single_post(post_id):
    session = Session(engine)
    try:
        post_select_stmt = select(Post).where(Post.id == post_id, Post.active == 1)
        post = session.scalars(post_select_stmt).one()
        return post
    except Exception as exc:
        current_app.logger.exception(str(exc))
        return {}
    finally:
        session.close()


def delete_single_post(post_id):
    session = Session(engine)
    try:
        post_select_stmt = select(Post).where(Post.id == post_id)
        post = session.scalars(post_select_stmt).one()
        post.active = False
        session.commit()
        return post
    except Exception as exc:
        current_app.logger.exception(str(exc))
        return {}
    finally:
        session.close()


def get_all_posts():
    session = Session(engine)
    try:
        post_select_stmt = select(Post).where(Post.active == 1)
        post = session.scalars(post_select_stmt).all()
        session.commit()
        return post
    except Exception as exc:
        current_app.logger.exception(str(exc))
        return []
    finally:
        session.close()


def authenticate(user, password):
    pass
