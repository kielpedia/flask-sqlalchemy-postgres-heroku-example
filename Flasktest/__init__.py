from __future__ import with_statement
from contextlib import closing
import sqlite3
from Flasktest.database import db_session
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

#configuration
DATABASE = '/tmp/flasktest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import Flasktest.views

def before_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db_session.remove()

if __name__ == '__main__':
  app.run()
