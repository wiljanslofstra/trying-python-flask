from ..main import app, db
from ..blog import routes
from flask import render_template, redirect

@app.route("/")
def index():
    return redirect('/blog')
