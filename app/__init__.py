"""Application initialization."""
import os
from flask import Flask, request, redirect, url_for, render_template, g
from flask_sqlalchemy import SQLAlchemy
import flask.ext.login as flask_login

app = Flask(__name__)
if os.path.exists("app/config/local.cfg"):
    app.config.from_pyfile('config/local.cfg', silent=True)
else:
    app.config.from_pyfile('sample.cfg', silent=True)

db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)
login_manager.login_view = "login"

from app import views, models  # noqa
