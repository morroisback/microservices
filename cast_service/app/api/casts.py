from fastapi import APIRouter, HTTPException

from app.api import db_manager
from app.api.models import CastIn, CastOut, CastUpdate


casts = APIRouter()


@casts.post("/", response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn) -> dict:
    cast_id = await db_manager.add_cast(payload)
    return {"id": cast_id, **payload.model_dump()}


@casts.get("/", response_model=list[CastOut])
async def get_casts() -> list[dict]:
    return await db_manager.get_all_casts()


@casts.get("/{id}/", response_model=CastOut)
async def get_cast(id: int) -> dict:
    cast = await db_manager.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail=f"Cast not found")
    return cast
