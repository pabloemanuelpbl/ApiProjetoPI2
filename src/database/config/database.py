import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

db = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#Base.metadata.create_all(bind=db)