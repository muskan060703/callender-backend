from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.routes import user
from app.routes import auth

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(user.router)
app.include_router(auth.router)
