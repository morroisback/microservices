from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager
from typing import AsyncIterator

from app.api.casts import casts
from app.api.db import metadata, database, engine

import os

metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    lifespan=lifespan, openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs"
)

app.include_router(casts, prefix="/api/v1/casts", tags=["casts"])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico")
async def favicon() -> FileResponse:
    file_name = "favicon.gif"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(
        path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name}
    )
