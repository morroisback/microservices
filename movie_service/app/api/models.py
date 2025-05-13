from pydantic import BaseModel


class MovieIn(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts_id: list[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: str | None = None
    plot: str | None = None
    genres: list[str] | None = None
    casts_id: list[int] | None = None
