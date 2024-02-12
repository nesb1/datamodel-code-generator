from __future__ import annotations

from pydantic import BaseModel, Field


class Item(BaseModel):
    bar: object = Field(None, title='Bar')
    foo: str = Field(..., title='Foo')
