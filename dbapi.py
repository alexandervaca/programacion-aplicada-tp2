import sqlite3
from sqlite3 import Error
from modelo import Disparo

class DBApi:
    conn = None

    def __init__(self):
        self.conectar()
        self.crearTablaDisparos()

    def conectar(self):
        try:
            self.conn = sqlite3.connect('torneo.db')
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def crearTablaDisparos(self):
        try:
            cursor = self.conn.cursor()

            cursor.execute('''CREATE TABLE disparos
                    ([generated_id] INTEGER PRIMARY KEY,[nro_participante] integer,[nombre] text,[apellido] text,'''+
                    '''[edad] integer,[sexo] text,[disp1] real,[disp2] real,[disp3] real,[mejor_disp] real,[prom_disp] real)''')
        except Error as e:
            print(e)

    def agregarDisparos(self,disparos):
        try:
            cursor = self.conn.cursor()

            for disparo in disparos:
                values = str(disparo.numero) + ',\'' + disparo.nombre + '\',\'' + disparo.apellido + '\',' + str(disparo.edad)
                values2 = ',\'' + disparo.sexo + '\',' + str(disparo.disp1) + ',' + str(disparo.disp2) + ',' + str(disparo.disp3)
                values3 = ',' + str(disparo.mejorDisp) + ',' + str(disparo.promedioDisp)

                cursor.execute('''INSERT INTO (nro_participante,nombre,apellido,edad,sexo,disp1,disp2,disp3,mejor_disp,prom_disp) disparos'''+
                ''' VALUES (''' + values + values2 + values3 + ''')''')
            
        except Error as e:
            print(e)

    def mostrarDisparos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('select * from disparos')
            disparosDB = cursor.fetchall()
            
            for disparoDB in disparosDB:
                print(str(disparoDB))
            
        except Error as e:
            print(e)

    pass
