from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, DisparoDB
from modelo import Disparo

#conexion a la base de datos
class DBApiAlchemy:

  def guardar(self,disparos):
    engine = create_engine('sqlite:///torneoAlchemy.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    for disparo in disparos:
      disparoDB = DisparoDB()
      disparoDB.nro_participante = disparo.numero
      disparoDB.nombre = disparo.nombre
      disparoDB.apellido = disparo.apellido
      disparoDB.edad = disparo.edad
      disparoDB.sexo = disparo.sexo
      disparoDB.disp1 = disparo.disp1
      disparoDB.disp2 = disparo.disp2
      disparoDB.disp3 = disparo.disp3
      disparoDB.mejor_disp = disparo.mejorDisp
      disparoDB.prom_disp = disparo.promedioDisp
      session.add(disparoDB)

    session.commit()

  def mostrarDisparos(self):
    engine = create_engine('sqlite:///torneoAlchemy.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    disparosDB = session.query(DisparoDB).all()
    for disparoDB in disparosDB:
      print(disparoDB)

