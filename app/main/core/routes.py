from ..main import app, db
from ..blog import routes
from flask import render_template

@app.route("/")
def index():
    result = db.engine.execute("SELECT * FROM blog")

    blogs = []

    for blog in result:
        blogs.append(blog)

    return ''.join(blogs)

    return render_template('index.html')
