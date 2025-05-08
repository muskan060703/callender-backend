from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.routes import user

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(user.router)
