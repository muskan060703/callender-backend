from fastapi import FastAPI, Depends
from app.schemas.user import UserCreate, ShowUser
from app.db.session import get_db, engine
from app.db.base import Base
from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.hashing import hash_password


app = FastAPI()

Base.metadata.create_all(engine) 
@app.post('/user', response_model=ShowUser)
def create_user(request:UserCreate, db: Session = Depends(get_db)):
    new_user = User(username = request.username, 
                    email = request.email,
                    password = hash_password(request.password), 
                    role = request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user