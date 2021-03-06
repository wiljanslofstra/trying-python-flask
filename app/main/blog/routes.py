from flask import render_template, abort
from ..main import app, db
from ..models.Blog import Blog

@app.route("/blog")
def blogs():
    blogs = Blog.query.order_by(Blog.published_at.desc()).all()
    return render_template('blog/blogs.html', blogs=blogs)

@app.route("/blog/<string:slug>")
def blog(slug):
    blog = Blog.query.filter_by(slug=slug).first()

    if (blog is None):
        abort(404)

    return render_template('blog/blog_post.html', blog=blog)
