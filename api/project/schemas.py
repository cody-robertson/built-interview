from marshmallow import Schema, fields, post_load
from project.models import BudgetCategory, BudgetItem


class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)

    @post_load
    def make_category(self, data, **kwargs):
        return BudgetCategory(**data)


class ItemSchema(Schema):
    id = fields.Int()
    value = fields.Decimal(required=True)
    category_id = fields.Int(required=True)

    @post_load
    def make_item(self, data, **kwargs):
        return BudgetItem(**data)
