from flask import Response, render_template, abort
from ..main import app
from ..models.Category import Category

@app.route("/category/<string:slug>")
def category(slug):
    category = Category.query.filter_by(slug=slug).first()

    if (category is None):
        abort(404)

    return render_template("category/category.html", category=category)

