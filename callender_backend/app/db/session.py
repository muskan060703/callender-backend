from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "sqlite:///./callender.db"

engine = create_engine(
   DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()