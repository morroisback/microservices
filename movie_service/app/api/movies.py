from fastapi import APIRouter, HTTPException

from app.api import db_manager
from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api.service import is_cast_present


movies = APIRouter()


@movies.post("/", response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn) -> dict:
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with id: {cast_id} not found")

    movie_id = await db_manager.add_movie(payload)
    return {"id": movie_id, **payload.model_dump()}


@movies.get("/", response_model=list[MovieOut])
async def get_movies() -> list[dict]:
    return await db_manager.get_all_movies()


@movies.get("/{id}/", response_model=MovieOut)
async def get_movie(id: int) -> dict:
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@movies.put("/{id}/", response_model=None)
async def update_movie(id: int, payload: MovieUpdate) -> None:
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.model_dump(exclude_unset=True)

    if "casts_id" in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with id: {cast_id} not found")

    movie_in_db = MovieIn(**movie)

    update_movie = movie_in_db.model_copy(update=update_data)

    return await db_manager.update_movie(id, update_movie)


@movies.delete("/{id}/", response_model=None)
async def delete_movie(id: int) -> None:
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return await db_manager.delete_movie(id)
