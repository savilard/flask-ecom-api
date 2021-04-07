from flask import Flask
from flask_admin import Admin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
admin = Admin(template_mode='bootstrap4')
db = SQLAlchemy()
marshmallow = Marshmallow(app)

admin.init_app(app)
