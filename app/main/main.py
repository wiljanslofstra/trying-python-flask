from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/app'
app.config['SECRET_KEY'] = 'MySuperRand!23SEcR3tKYE!'

db = SQLAlchemy(app)
Base = declarative_base()
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

from .core import routes, jinja_setup

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
