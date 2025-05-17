from sqlalchemy.orm import Session
from app.models import ExampleModel
from app.schemas import ExampleCreateSchema

# Service function to get all examples
def get_examples(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ExampleModel).offset(skip).limit(limit).all()

# Service function to create a new example
def create_example(db: Session, example: ExampleCreateSchema):
    db_example = ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

# Service function to get a specific example by ID
def get_example_by_id(db: Session, example_id: int):
    return db.query(ExampleModel).filter(ExampleModel.id == example_id).first()

# Service function to update an example
def update_example(db: Session, example_id: int, example: ExampleCreateSchema):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example:
        for key, value in example.dict().items():
            setattr(db_example, key, value)
        db.commit()
        db.refresh(db_example)
    return db_example

# Service function to delete an example
def delete_example(db: Session, example_id: int):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example