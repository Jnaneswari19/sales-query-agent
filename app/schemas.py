from pydantic import BaseModel
from typing import Optional

class CustomerSchema(BaseModel):
    id: int
    name: str
    region: str
    segment: str

    class Config:
        orm_mode = True
