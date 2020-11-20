import sqlite3
from sqlite3 import Error
from modelo import Disparo

class DBApi:
    conexion = None

    def __init__(self):
        self.conectarDB()
        self.crearTablaDisparos()

    def conectarDB(self):
        try:
            self.conexion = sqlite3.connect('torneo.db')
        except Error as e:
            print(e)
        finally:
            if self.conexion:
                self.conexion.close()

    def crearTablaDisparos(self):
        try:
            self.conexion = sqlite3.connect('torneo.db')
            cursor = self.conexion.cursor()

            cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='disparos' ''')

            #if the count is 1, then table exists
            if cursor.fetchone()[0] == 1: 
                print('Ya existe la tabla \'disparos\'.')
            else:
                cursor.execute('''CREATE TABLE disparos
                    ([generated_id] INTEGER PRIMARY KEY,[nro_participante] integer,[nombre] text,[apellido] text,'''+
                    '''[edad] integer,[sexo] text,[disp1] real,[disp2] real,[disp3] real,[mejor_disp] real,[prom_disp] real)''')

            self.conexion.commit()
        
        except Error as e:
            print(e)
        finally:
            if self.conexion:
                self.conexion.close()

    def guardarEnDB(self,disparos):
        try:
            self.conexion = sqlite3.connect('torneo.db')
            cursor = self.conexion.cursor()

            for disparo in disparos:
                values = str(disparo.numero) + ',\'' + disparo.nombre + '\',\'' + disparo.apellido + '\',' + str(disparo.edad)
                values2 = ',\'' + disparo.sexo + '\',' + str(disparo.disp1) + ',' + str(disparo.disp2) + ',' + str(disparo.disp3)
                values3 = ',' + str(disparo.mejorDisp) + ',' + str(disparo.promedioDisp)

                cursor.execute('''INSERT INTO disparos(nro_participante,nombre,apellido,edad,sexo,disp1,disp2,disp3,mejor_disp,prom_disp)'''+
                ''' VALUES (''' + values + values2 + values3 + ''')''')

                self.conexion.commit()

        except Error as e:
            print(e)
        finally:
            if self.conexion:
                self.conexion.close()

    def mostrarDisparos(self):
        try:
            self.conexion = sqlite3.connect('torneo.db')
            cursor = self.conexion.cursor()

            cursor.execute('''SELECT * FROM disparos''')
            disparosDB = cursor.fetchall()
            
            for disparoDB in disparosDB:
                print(str(disparoDB))
            
            self.conexion.commit()

        except Error as e:
            print(e)
        finally:
            if self.conexion:
                self.conexion.close()

    pass
