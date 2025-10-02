import mysql.connector
from carrera import Carrera

class CarreraDAO:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="universidad"
        )
        
    def create(self, c):
        cur = self.__conn.cursor()
        sql = "INSERT INTO carreras (nombre, duracion, id) VALUES (%s, %s, %s)"
        cur.execute(sql, (c.nombre, c.duracion, c.id_))
        self.__conn.commit()
        cur.close()
    
    def read(self, id_):
        pass
    
    def update(self, c):
        pass
    
    def delete(self, id_):
        pass
    
    def fetchall(self):
        pass


