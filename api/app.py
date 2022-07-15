from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from project import get_db_uri, BudgetCategory, BudgetItem
from markupsafe import escape

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app)


@app.get("/budget-categories/")
def list_categories():
    pass


@app.post("/budget-categories/")
def add_category():
    pass


@app.get("/budget-categories/<int:category_id>/")
def get_category(category_id: str):
    category_id = escape(category_id)


@app.put("/budget-categories/<int:category_id>/")
def update_category(category_id: str):
    category_id = escape(category_id)


@app.delete("/budget-categories/<int:category_id>/")
def delete_category(category_id: str):
    category_id = escape(category_id)


@app.get("/budget-items/")
def list_budget_items():
    pass


@app.post("/budget-items/")
def add_budget_item():
    pass


@app.get("/budget-items/<int:item_id>/")
def get_item(item_id: str):
    item_id = escape(item_id)


@app.post("/budget-items/<int:item_id>/")
def get_item(item_id: str):
    item_id = escape(item_id)


@app.delete("/budget-items/<int:item_id>/")
def get_item(item_id: str):
    item_id = escape(item_id)


if __name__ == "__main__":
    app.run(debug=True)
