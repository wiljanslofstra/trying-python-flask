from ..main import db

class Form(db.Model):
    __tablename__ = 'forms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    message = db.Column(db.Text(255))
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return self.email
