from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/app'
app.config['SECRET_KEY'] = 'MySuperRand!23SEcR3tKYE!'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_TRACKABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_EMAIL_SENDER'] = 'wiljanslofstra@gmail.com'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'SVPER#12S3cR3t!PA55W0rdSal$1294ekjd349!#$)dfadf34dfacvjjekr'

app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '2f9798943d60d7'
app.config['MAIL_PASSWORD'] = 'b37b835a6cfcf6'

db = SQLAlchemy(app)
Base = declarative_base()
csrf = CSRFProtect(app)
migrate = Migrate(app, db)
mail = Mail(app)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db.engine))

from .models.Auth import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from .core import routes, jinja_setup

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
