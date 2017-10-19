from flask import Response, render_template
from ..main import app
from ..models.Category import Category
from pprint import pprint

@app.route("/category/<string:slug>")
def category(slug):
    category = Category.query.filter_by(slug=slug).first()
    return render_template("category/category.html", category=category)

