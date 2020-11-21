from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Disparo

#conexion a la base de datos
class DBApiAlchemy:

  def guardar(self,disparos):
    engine = create_engine('sqlite:///torneoAlchemy.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    for disparo in disparos:
      disparoDB = Disparo()
      disparoDB.nro_participante = disparo.nro_participante
      disparoDB.nombre = disparo.nombre
      disparoDB.apellido = disparo.apellido
      disparoDB.edad = disparo.edad
      disparoDB.sexo = disparo.sexo
      disparoDB.disp1 = disparo.disp1
      disparoDB.disp2 = disparo.disp2
      disparoDB.disp3 = disparo.disp3
      disparoDB.mejor_disp = disparo.mejor_disp
      disparoDB.prom_disp = disparo.prom_disp
      session.add(disparoDB)

    session.commit()

  def mostrarDisparos(self):
    engine = create_engine('sqlite:///torneoAlchemy.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    disparosDB = session.query(Disparo).all()
    for disparoDB in disparosDB:
      print(disparoDB)

