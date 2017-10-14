from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, length
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), length(max=255)])
    email = EmailField('email', validators=[DataRequired(), Email(), length(max=255)])
    message = TextAreaField('message', validators=[DataRequired(), length(max=2000)])
