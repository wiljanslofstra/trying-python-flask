from ..main import app, db
from ..error import routes
from ..blog import routes
from ..contact import routes
from ..category import routes
from flask import render_template, redirect
from flask_security import login_required

@app.route("/")
def index():
    return redirect('/blog')

@app.route("/secret")
@login_required
def secret():
    return render_template("secret.html")
