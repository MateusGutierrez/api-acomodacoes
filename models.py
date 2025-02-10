from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Accomodation(Base):
    __tablename__ = 'acomodacoes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    img = Column(String)
    preco = Column(Integer)
    localizacao = Column(String)
    descricao = Column(String)