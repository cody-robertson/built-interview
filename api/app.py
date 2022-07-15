from flask import Flask, request, jsonify, logging
from flask_sqlalchemy import SQLAlchemy
from project import get_db_uri, BudgetCategory, BudgetItem, CategorySchema, ItemSchema
from markupsafe import escape
from functools import wraps

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app)
logger = logging.create_logger(app)


def handle_error(fun):
    @wraps(fun)
    def inner(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            logger.exception("Error in inner function")
            return str(e), 500
    return inner


@app.get("/budget-categories/")
@handle_error
def list_categories():
    categories_list = db.session.query(BudgetCategory).all()
    result = categories_schema.dump(categories_list)
    return jsonify(result)


@app.post("/budget-categories/")
@handle_error
def add_category():
    result = category_schema.load(request.get_json())
    db.session.add(result)
    db.session.commit()
    return category_schema.dump(result)


@app.get("/budget-categories/<int:category_id>/")
@handle_error
def get_category(category_id: str):
    category_id = escape(category_id)
    categories = db.session.query(BudgetCategory).filter_by(id=category_id).all()

    if not len(categories) == 1:
        return "", 404

    return category_schema.dump(categories[0])


@app.put("/budget-categories/<int:category_id>/")
@handle_error
def update_category(category_id: str):
    category_id = escape(category_id)
    categories = db.session.query(BudgetCategory).filter_by(id=category_id).all()

    if not len(categories) == 1:
        return "", 404

    validated_data = category_schema.load(request.get_json())
    category = categories[0]
    category.name = validated_data.name
    db.session.commit()

    return category_schema.dump(category)


@app.delete("/budget-categories/<int:category_id>/")
@handle_error
def delete_category(category_id: str):
    category_id = escape(category_id)
    category = db.session.query(BudgetCategory).filter(BudgetCategory.id == category_id).first()

    db.session.delete(category)
    db.session.commit()
    return "", 200


@app.get("/budget-items/")
@handle_error
def list_budget_items():
    items = db.session.query(BudgetItem).all()
    result = items_schema.dump(items)
    return jsonify(result)


@app.post("/budget-items/")
@handle_error
def add_budget_item():
    pass


@app.get("/budget-items/<int:item_id>/")
@handle_error
def get_item(item_id: str):
    item_id = escape(item_id)


@app.post("/budget-items/<int:item_id>/")
@handle_error
def update_item(item_id: str):
    item_id = escape(item_id)


@app.delete("/budget-items/<int:item_id>/")
@handle_error
def delete_item(item_id: str):
    item_id = escape(item_id)


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


if __name__ == "__main__":
    app.run(debug=True)
