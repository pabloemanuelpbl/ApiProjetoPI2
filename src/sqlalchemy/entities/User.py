from sqlalchemy import  Column, Integer, String
from src.sqlalchemy.config.database import Base

class Test(Base):
    __tablename__ = "testes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)