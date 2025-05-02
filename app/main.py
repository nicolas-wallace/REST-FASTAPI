from fastapi import FastAPI
from routes import router
from database import Base, engine
from models import Item

app = FastAPI()
app.include_router(router)
Base.metadata.create_all(bind=engine)