from sqlalchemy.orm import sessionmaker
from database.postgres import engine

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)