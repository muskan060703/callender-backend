from sqlalchemy import Column, Integer, String, Enum, DateTime 
from sqlalchemy.sql import func
from app.db.base import Base
import enum 

class OrganisationType(str, enum.Enum):
    lawyer = "lawyer"
    clinic = "clinic"
    default = "defualt"
    

class Organisation(Base):
    __tablename__ = "organisation"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable=False, unique=True, nullable=False)
    type = Column(Enum(OrganisationType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())