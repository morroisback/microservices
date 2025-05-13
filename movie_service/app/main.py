from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager
from typing import AsyncIterator

from app.api.db import metadata, database, engine
from app.api.movies import movies

import os

metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    lifespan=lifespan, openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs"
)

app.include_router(movies, prefix="/api/v1/movies", tags=["movies"])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico")
async def favicon() -> FileResponse:
    file_name = "favicon.gif"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(
        path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name}
    )
