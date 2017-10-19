from ..main import app, db
from ..blog import routes
from ..contact import routes
from ..category import routes
from flask import render_template, redirect

@app.route("/")
def index():
    return redirect('/blog')
