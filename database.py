import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# @contextlib.contextmanager
# Depends를 사용하므로 이중으로 contextmanager가 적용되지 않도록 제거해준다.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()