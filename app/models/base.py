from tortoise.models import Model
from tortoise import fields

class BaseWithId(Model):
    id = fields.IntField(pk=True)


class BaseWithDatetime(BaseWithId):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)