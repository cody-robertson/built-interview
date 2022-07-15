import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from project.utils import get_test_db_uri
from project import BudgetCategory


@pytest.fixture(scope="session")
def db():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = get_test_db_uri()
    return SQLAlchemy(app)


@pytest.fixture(scope="session")
def setup_database(db):
    BudgetCategory.metadata = db.metadata
    BudgetCategory.metadata.create_all()

    yield

    BudgetCategory.metadata.drop_all()
