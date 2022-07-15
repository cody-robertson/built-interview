from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils import get_db_uri

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app)


class BudgetCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)


class BudgetAmount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    amount = db.Column(db.Numeric(precision=15, scale=2, asdecimal=True))
    category = db.relationship(
        "BudgetCategory", backref=db.backref("budget_amounts", lazy=True)
    )


class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Numeric(precision=15, scale=2, asdecimal=True))
    category = db.relationship(
        "BudgetCategory", backref=db.backref("budget_items", lazy=True)
    )
