from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API CRUD com FastAPI + Swagger")

# Dependência para pegar o DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    """Endpoint raiz para verificar se a API está funcionando"""
    return {
        "message": "API CRUD com FastAPI está funcionando!",
        "status": "healthy",
        "endpoints": {
            "items": "/items/",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

@app.post("/items/", response_model=schemas.ItemOut)
def criar_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[schemas.ItemOut])
def listar_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.get("/items/{item_id}", response_model=schemas.ItemOut)
def obter_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.ItemOut)
def atualizar_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.ItemOut)
def deletar_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db_item