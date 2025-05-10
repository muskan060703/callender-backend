from fastapi import APIRouter
from app.schemas.user import UserCreate, ShowUser
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.hashing import hash_password
from fastapi import Depends
from app.services.user import createUser

router = APIRouter(prefix="/user", tags=["User"])


@router.post(
    "/",
    response_model=ShowUser,
)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return createUser(request, db)
