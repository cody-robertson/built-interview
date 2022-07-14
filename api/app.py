from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import get_db_uri

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app)


@app.route("/budget-categories/", methods=["GET", "POST"])
def list_categories():
    pass


@app.route("/budget-categories/:category_id", methods=["GET", "POST", "DELETE"])
def get_category(category_id: str):
    pass


@app.route("/budget-items/", methods=["GET", "POST"])
def list_budget_items():
    pass


@app.route("/budget-items/:item_id", methods=["GET", "POST", "DELETE"])
def get_item(item_id: str):
    pass


if __name__ == "__main__":
    app.run(debug=True)
