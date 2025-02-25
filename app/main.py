# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, users, items

# Create all tables in the database if they do not exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fully Featured FastAPI Backend",
    description="An end-to-end FastAPI backend with authentication, user, and item management.",
    version="1.0.0"
)

# Include the routers for the different endpoints.
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fully Featured FastAPI Backend"}
