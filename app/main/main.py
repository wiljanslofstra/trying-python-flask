from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/app'
app.config['SECRET_KEY'] = 'MySuperRand!23SEcR3tKYE!'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from .core import routes, jinja_setup

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
