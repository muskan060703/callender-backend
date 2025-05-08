from fastapi import FastAPI, Depends
from app.schemas.user import UserCreate
from app.db.session import get_db, engine
from app.db.base import Base
from sqlalchemy.orm import Session
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(engine) 
@app.post('/user')
def create_user(request:UserCreate, db: Session = Depends(get_db)):
    
    new_user = User(**request.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user