from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.table import Table
from app.schemas.table import Table as TableSchema, TableCreate

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[TableSchema])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.post("/", response_model=TableSchema)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/{id}")
def delete_table(id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(table)
    db.commit()
    return {"message": "Table deleted"}