from fastapi import APIRouter
from app.schemas.user import UserCreate, ShowUser
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.hashing import hash_password
from fastapi import Depends

router = APIRouter()


@router.post("/user", response_model=ShowUser, tags=["user"])
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password),
        role=request.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
