from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Item
from database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class ItemCreate(BaseModel):
    nome: str
    descricao: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(nome=item.nome, descricao=item.descricao)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    print("POST /items", db_item.__dict__)
    return db_item

@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    print("GET /items")
    return items

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    print("DELETE /items", item_id)
    return {"message": "Item deleted"}

    