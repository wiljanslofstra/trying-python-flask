from ..main import db

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    slug = db.Column(db.String)
    content = db.Column(db.Text)
    published_at = db.Column(db.DateTime)
