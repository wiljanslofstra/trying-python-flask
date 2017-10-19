from ..main import db
from .Blog import Blog

association_table = db.Table('categories_blogs_association', db.Model.metadata,
    db.Column('blogs_id', db.Integer, db.ForeignKey('blogs.id')),
    db.Column('categories_id', db.Integer, db.ForeignKey('categories.id'))
)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    slug = db.Column(db.String)
    blogs = db.relationship("Blog", secondary=association_table, backref="categories")

    def __repr__(self):
        return self.title
