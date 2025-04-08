from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    table_id = Column(Integer, ForeignKey("table.id"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    