# app/models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"  # Name of the table in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key with index for faster lookups
    username = Column(String, unique=True, index=True)  # Unique username
    email = Column(String, unique=True, index=True)     # Unique email address
    hashed_password = Column(String)                    # Hashed password storage
    is_active = Column(Boolean, default=True)           # Whether the user is active
    items = relationship("Item", back_populates="owner") # Relationship with items

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)                  # Item title
    description = Column(String, index=True)            # Item description
    owner_id = Column(Integer, ForeignKey("users.id"))  # Foreign key linking to the user
    owner = relationship("User", back_populates="items") # Relationship to the User
