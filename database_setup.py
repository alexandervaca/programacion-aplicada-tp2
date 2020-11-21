import sys
from sqlalchemy import Column, Numeric, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Disparo(Base):
    __tablename__ = 'disparos'

    id = Column(Integer,primary_key=True)
    nro_participante = Column(Integer,nullable=True)
    nombre = Column(String(100),nullable=True)
    apellido = Column(String(100),nullable=True)
    edad = Column(Integer,nullable=True)
    sexo = Column(String(10),nullable=True)
    disp1 = Column(String(20),nullable=True)
    disp2 = Column(String(20),nullable=True)
    disp3 = Column(String(20),nullable=True)
    mejor_disp = Column(String(20),nullable=True)
    prom_disp = Column(String(20),nullable=True)

engine = create_engine('sqlite:///torneoAlchemy.db')
Base.metadata.create_all(engine)
