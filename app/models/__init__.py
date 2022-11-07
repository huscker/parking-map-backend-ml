from tortoise import fields
from .base import BaseWithDatetime


class TestModel(BaseWithDatetime):
    name = fields.IntField()

    def find_by_id(self, id: int):
        return self.get(id=id)

    class Meta:
        table = "test_model"
