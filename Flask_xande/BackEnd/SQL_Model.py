import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship 
from SQL_Engine import engine

Base = declarative_base()

# Tabela do Usuario
class Usuario(Base):
    __tablename__ = 'Usuario'
    
    Id_Usuario: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    Nome_Usuario: Mapped[str] = mapped_column(String(100))
    Email_Usuario: Mapped[str] = mapped_column(String(100))
    Senha_Usuario: Mapped[str] = mapped_column(String(255))
    Status_Usuario: Mapped[str] = mapped_column(String(20))
    Data_Registro: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    Ultimo_Login: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    Assinatura: Mapped[Boolean] = mapped_column(Boolean(), default=True)
    Pagamento: Mapped[list["Pagamento"]] = relationship("Pagamento", back_populates="Usuario", cascade="all, delete-orphan")
    Favoritos: Mapped[list["Item"]] = relationship(secondary="Favoritos", back_populates="Usuarios")



class Autor(Base):
    __tablename__ = 'Autor'

    id_Autor: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Nome_Autor: Mapped[str] = mapped_column(String(100))
    Nacionalidade_Autor: Mapped[str] = mapped_column(String(100))
    Itens: Mapped[list["Item"]] = relationship("Item", back_populates="Autor", cascade="all, delete-orphan")

class Categoria(Base):
    __tablename__ = 'Categoria'

    Id_Categoria: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Nome_Categorias: Mapped[str] = mapped_column(String(100))
    Descricao_Categoria: Mapped[str] = mapped_column(String(200))
    Itens: Mapped[list["Item"]] = relationship("Item", back_populates="Categoria", cascade="all, delete-orphan")

class Item(Base):
    __tablename__ = 'Item'

    Id_Item: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Titulo_Item: Mapped[str] = mapped_column(String(200))
    Descricao_Item: Mapped[str] = mapped_column(String(200))
    Data_Publicacao: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    Autor_Id: Mapped[int] = mapped_column(ForeignKey("Autor.id_Autor"))
    Autor: Mapped["Autor"] = relationship("Autor", back_populates="Itens")
    Categoria_Id: Mapped[int] = mapped_column(ForeignKey("Categoria.Id_Categoria"))
    Categoria: Mapped["Categoria"] = relationship("Categoria", back_populates="Itens")
    Usuarios: Mapped[list["Usuario"]] = relationship(secondary="Favoritos", back_populates="Favoritos")

Favoritos = Table(
    "Favoritos",
    Base.metadata,
    Column("Usuario_Id", ForeignKey("Usuario.Id_Usuario")),
    Column("Item_Id", ForeignKey("Item.Id_Item")),
)

class Pagamento(Base):
    __tablename__ = 'Pagamento'

    id_pagamento: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Usuario_Id: Mapped[int] = mapped_column(ForeignKey("Usuario.Id_Usuario"))
    Usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="Pagamento")
    Data_Pagamento: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    Valor_Pagamento: Mapped[float] = mapped_column()
    Metodo_Pagamento: Mapped[str] = mapped_column(String(50))

if __name__ == "__main__":
    Base.metadata.create_all(engine)
