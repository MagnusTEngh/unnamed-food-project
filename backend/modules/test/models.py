from sqlalchemy import Column, Integer, String, create_engine

from db.base import Base

class TestTable(Base):
    __tablename__ = "testtable"
    id = Column(Integer, autoincrement=True, primary_key=True)
    message = Column(String)