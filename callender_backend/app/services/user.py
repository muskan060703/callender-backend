from app.models.user import User
from sqlalchemy.orm import Session
from app.auth.hashing import hash_password


def createUser(request, db: Session):
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
