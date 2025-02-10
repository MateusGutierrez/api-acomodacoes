from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional, Annotated
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from dummy import dummy
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def add_accomodation(db: Session):
    if db.query(models.Accomodation).count() == 0:
        for data in dummy:
            accomodation = models.Accomodation(
                id=data['id'],
                nome=data['nome'],
                img=data['img'],
                preco=data['preco'],
                localizacao=data['localizacao'],
                descricao=data['descricao']
            )
            db.add(accomodation)
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
        add_accomodation(db)
    finally:
        db.close()

class Accomodation(BaseModel):
    id: int
    nome: str
    img: str
    preco: int
    localizacao: str
    descricao: str

@app.get("/acomodacoes", response_model=List[Accomodation])
async def get_accomodations(
    db: db_dependency,
    cidade: Optional[str] = Query(None, description="Get accomodation by city")
):
    query = db.query(models.Accomodation)
    if cidade:
        query = query.filter(models.Accomodation.localizacao.ilike(f"%{cidade}%"))
    return query.all()

@app.get("/acomodacoes/{id}", response_model=Accomodation)
def get_accomodation_by_id(id: int, db: db_dependency):
    accomodation = db.query(models.Accomodation).filter(models.Accomodation.id == id).first()
    if not accomodation:
        raise HTTPException(status_code=404, detail="Not found")
    return accomodation
