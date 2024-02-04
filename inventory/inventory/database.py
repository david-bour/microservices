import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USERNAME=os.environ.get("POSTGRES_USERNAME", "postgres")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_DATABASE=os.environ.get("POSTGRES_DATABASE", "postgres")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()