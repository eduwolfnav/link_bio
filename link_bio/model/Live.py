# pip install reflex[db]
# pip install greenlet

import reflex as rx
from sqlmodel import SQLModel, Field

class Live(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    live: bool
    title: str