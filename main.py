from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional, Annotated
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from dummy import dummy 

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def inserir_acomodacoes(db: Session):
    if db.query(models.Acomodacoes).count() == 0:
        for data in dummy:
            acomodacao = models.Acomodacoes(
                id=data['id'],
                nome=data['nome'],
                img=data['img'],
                preco=data['preco'],
                localizacao=data['localizacao']
            )
            db.add(acomodacao)
        db.commit()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.on_event("startup")
def startup_db():
    db = SessionLocal()
    try:
        models.Base.metadata.create_all(bind=engine)
        inserir_acomodacoes(db)
    finally:
        db.close()

class Acomodacoes(BaseModel):
    id: int
    nome: str
    img: str
    preco: int
    localizacao: str

@app.get("/acomodacoes", response_model=List[Acomodacoes])
async def get_acomodacoes(
    db: db_dependency,
    cidade: Optional[str] = Query(None, description="Filtrar por cidade")
):
    query = db.query(models.Acomodacoes)
    if cidade:
        query = query.filter(models.Acomodacoes.localizacao.ilike(f"%{cidade}%"))
        print(query.all())
    return query.all()

@app.get("/acomodacoes/{id}", response_model=Acomodacoes)
def obter_acomodacao(id: int, db: db_dependency):
    acomodacao = db.query(models.Acomodacoes).filter(models.Acomodacoes.id == id).first()
    if not acomodacao:
        raise HTTPException(status_code=404, detail="Acomodação não encontrada")
    return acomodacao
