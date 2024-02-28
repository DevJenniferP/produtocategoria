import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import (Column, Uuid, String, DateTime, Boolean, DECIMAL, Integer, func, ForeignKey)

motor = create_engine("sqlite:///banco_de_dados.sqliter", echo=False)

class Base(DeclarativeBase):
    pass

class Datasmixin():
    dta_cadastro = Column(DateTime, onupdate=func.now(), server_default=func.now(), nullable=False)
    dta_atualizacao = Column(DateTime, onupdate=func.now(), default=func.now(), nullable=False)

class Categoria(Base, Datasmixin):
    __tablename__ = "tbl_categoria"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4())
    none = Column(String(256), nulable=False)

    lista_de_produtos =relationship("Produto", back_populates="categorias", cascade="all, delete-orphan", lazy="seletin")
class Produto(Base, Datasmixin):
    __tablename__ = "tbl_produto"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(256), default=False)
    preco = Column(DECIMAL, nullable=False)
    estoque = Column(Integer, default=True)
    categoria_id = Column(Uuid(as_uuid=True), ForeignKey("tbl_categoria.id"))

    categoria =relationship(Categoria, back_populates="lista_de_produtos")