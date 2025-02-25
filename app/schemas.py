# app/schemas.py
from pydantic import BaseModel
from typing import Optional, List

# -------------------
# User Schemas
# -------------------

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  # Plain password for registration (will be hashed)

class User(UserBase):
    id: int
    is_active: bool
    items: List['Item'] = []  # List of items associated with the user

    class Config:
        orm_mode = True  # Allow Pydantic to work with ORM objects

# -------------------
# Item Schemas
# -------------------

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass  # Same fields as ItemBase; used when creating an item

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# -------------------
# Token Schemas (for authentication)
# -------------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# This is to support forward references in Pydantic models.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .schemas import Item
