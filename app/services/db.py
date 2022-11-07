from tortoise import Tortoise
from settings import DB_CONNECTION_STRING

# TODO: select classes
async def init_db():
    await Tortoise.generate_schemas(safe=True)


async def connect_db():
    await Tortoise.init(db_url=DB_CONNECTION_STRING, modules={'models': ['models']})
