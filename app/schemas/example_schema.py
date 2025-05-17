from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a new example
class ExampleCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None

# Schema for reading an example, including database-generated fields
class ExampleSchema(ExampleCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models