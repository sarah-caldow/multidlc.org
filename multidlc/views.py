from multidlc import app
from multidlc.src.application import multidlc_database
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

@app.route('/')
def index():
    db = multidlc_database.get_db()
    return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/books')
def books():
	return render_template('books.html')

@app.route('/instrumentation')
def instrumentation():
	return render_template('instrumetation.html')

@app.route('/literature')
def literature():
	return render_template('literature.html')

@app.route('/terminology')
def terminology():
	return render_template('terminology.html')

@app.route('/tools')
def tools():
	return render_template('tools.html')