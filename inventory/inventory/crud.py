from sqlalchemy.orm import Session
from . import models, schemas

def get_item(db: Session, name: str):
    return db.query(models.Item).filter(models.Item.name == name).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    item = models.Item(**item.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
