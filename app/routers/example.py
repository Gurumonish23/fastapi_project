from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.dependencies import get_query_token, verify_user
from app.schemas import ExampleSchema, ExampleCreateSchema
from app.models import ExampleModel
from app.database import get_db

# Create a router for example endpoints
router = APIRouter(
    prefix="/examples",
    tags=["examples"],
    dependencies=[Depends(get_query_token)]
)

# Get all examples
@router.get("/", response_model=List[ExampleSchema])
def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    examples = db.query(ExampleModel).offset(skip).limit(limit).all()
    return examples

# Create a new example
@router.post("/", response_model=ExampleSchema)
def create_example(example: ExampleCreateSchema, db: Session = Depends(get_db)):
    db_example = ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

# Get a specific example by ID
@router.get("/{example_id}", response_model=ExampleSchema)
def read_example(example_id: int, db: Session = Depends(get_db)):
    example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return example

# Update an example
@router.put("/{example_id}", response_model=ExampleSchema)
def update_example(example_id: int, example: ExampleCreateSchema, db: Session = Depends(get_db)):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    for key, value in example.dict().items():
        setattr(db_example, key, value)
    db.commit()
    db.refresh(db_example)
    return db_example

# Delete an example
@router.delete("/{example_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_example(example_id: int, db: Session = Depends(get_db)):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    db.delete(db_example)
    db.commit()
    return None