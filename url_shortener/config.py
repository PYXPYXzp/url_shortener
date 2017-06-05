import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'url_shortener'),
    USERNAME = 'admin',
    PASSWORD = 'admin',
    SECRET_KEY = '1234'
))
app.config.from_envvar('URL_SHORTENER_SETTINGS', silent=True)