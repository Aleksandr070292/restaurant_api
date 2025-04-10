from sqlalchemy import Column, Integer, String
from app.database import Base

class Table(Base):
    __tablename__ = "table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String, nullable=False)