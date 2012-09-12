from Flasktest import app
from Flasktest.database import db_session
from Flasktest.models import Entry
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash



@app.route('/')
def show_entries():
  entries = Entry.query.all()
  return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
	abort(401)
  entry = Entry(request.form['title'], request.form['text'])
  db_session.add(entry)
  db_session.commit()
  flash('New entry was succesfully posted')
  return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
	if request.form['username'] != app.config['USERNAME']:
		error = 'Invalid Username'
	elif request.form['password'] != app.config['PASSWORD']:
		error = 'Invalid password'
	else:
		session['logged_in'] = True
		flash('You were logged in')
		return redirect(url_for('show_entries'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('show_entries'))
