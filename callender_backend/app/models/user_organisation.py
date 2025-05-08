from sqlalchemy import Column, Integer, ForeignKey, Table 
from app.db.base import Base

class UserOrganisation(Base):
    __tablename__ = "user_organisation"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    organisation_id = Column(Integer, ForeignKey("organisation.id"))
    
    