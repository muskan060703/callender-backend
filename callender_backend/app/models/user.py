from sqlalchemy import Column, Integer, String, DateTime 
from app.db.base import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)