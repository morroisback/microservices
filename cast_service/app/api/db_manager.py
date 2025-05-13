from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database


async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.model_dump())
    return await database.execute(query=query)


async def get_all_casts():
    query = casts.select()
    return await database.fetch_all(query=query)


async def get_cast(id: int):
    query = casts.select().where(casts.c.id == id)
    return await database.fetch_one(query=query)
