from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

MYSQL_HOST = os.environ.get("MYSQL_HOST", "")
MYSQL_PORT = os.environ.get("MYSQL_PORT", 3306)
MYSQL_DB = os.environ.get("MYSQL_DB", "")
MYSQL_USER = os.environ.get("MYSQL_USER", "")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+mysqldb://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}:${MYSQL_PORT}/${MYSQL_DB}"
db = SQLAlchemy(app)


class BudgetCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)


class BudgetAmount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    amount = db.Column(db.Numeric(precision=2, asdecimal=True))
    category = db.relationship('BudgetCategory', backref=db.backref('budget_amounts', lazy=True))


class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Numeric(precision=2, asdecimal=True))
    category = db.relationship('BudgetCategory', backref=db.backref('budget_items', lazy=True))
