from flask import Flask, request, jsonify, logging
from flask_sqlalchemy import SQLAlchemy
from project import get_db_uri, BudgetCategory, BudgetItem, CategorySchema, ItemSchema
from markupsafe import escape
from functools import wraps
import boto3
from botocore.config import Config

boto_config = Config(
    region_name='us-east-1',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
db = SQLAlchemy(app)
logger = logging.create_logger(app)

endpoint_url = "http://localstack:4566"
kinesis = boto3.client("kinesis", endpoint_url=endpoint_url,
    aws_access_key_id="ACCESS_KEY",
    aws_secret_access_key="SECRET_KEY",
    aws_session_token="SESSION_TOKEN",
    config=boto_config
)


def handle_error(fun):
    @wraps(fun)
    def inner(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            logger.exception("Error in inner function")
            return str(e), 500
    return inner


@app.get('/')
@handle_error
def kinesis_test():
    response = kinesis.list_streams(Limit=123)
    return jsonify(response)


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
    result = item_schema.load(request.get_json())
    db.session.add(result)
    db.session.commit()
    return item_schema.dump(result)


@app.get("/budget-items/<int:item_id>/")
@handle_error
def get_item(item_id: str):
    item_id = escape(item_id)
    items = db.session.query(BudgetItem).filter_by(id=item_id).all()

    if not len(items) == 1:
        return "", 404

    return item_schema.dump(items[0])


@app.put("/budget-items/<int:item_id>/")
@handle_error
def update_item(item_id: str):
    item_id = escape(item_id)
    items = db.session.query(BudgetItem).filter_by(id=item_id).all()

    if not len(items) == 1:
        return "", 404

    validated_data = item_schema.load(request.get_json())
    item = items[0]
    item.value = validated_data.value
    item.category_id = validated_data.category_id
    db.session.commit()

    return item_schema.dump(item)


@app.delete("/budget-items/<int:item_id>/")
@handle_error
def delete_item(item_id: str):
    item_id = escape(item_id)
    item = db.session.query(BudgetItem).filter(BudgetItem.id == item_id).first()

    db.session.delete(item)
    db.session.commit()
    return "", 200


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


if __name__ == "__main__":
    app.run(debug=True)
