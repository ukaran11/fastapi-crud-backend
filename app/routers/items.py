# app/routers/items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, utils

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.post("/", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(utils.get_current_user)  # Requires authentication
):
    return crud.create_item(db=db, item=item, user_id=current_user.id)

@router.get("/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
