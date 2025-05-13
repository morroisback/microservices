import os

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

casts = Table(
    "casts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("nationality", String(20)),
)

database = Database(DATABASE_URL)
