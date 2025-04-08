from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tables, reservations

app = FastAPI(title="Restaurant Reservation API")

Base.metadata.create_all(bind=engine)

app.include_router(tables.router)
app.include_router(reservations.router)
