from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from datetime import timedelta, datetime
from sqlalchemy.sql import text

def check_reservation_conflict(db: Session, table_id: int, start_time: datetime, duration: int):
    end_time = start_time + timedelta(minutes=duration)
    existing_reservations = db.query(Reservation).filter(
        Reservation.table_id == table_id,
        Reservation.reservation_time < end_time,
        (Reservation.reservation_time + (Reservation.duration_minutes * text("INTERVAL '1 minute'"))) > start_time
    ).all()
    return len(existing_reservations) > 0