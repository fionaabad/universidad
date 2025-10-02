import mysql.connector
from carrera import Carrera

class CarreraDAO:
    def __init__(self, conn):
        self.__conn = conn
        
    def create(self, c):
        
    def read(self, id_):
        pass
    
    def update(self, c):
        sql = "UPDATE carrera SET nombre =%s, duracion = %s, WHERE id = %s"
        valores = (c.GetNombre(), c.GetDuracion(), c.GetId())
        self.cursor.execute(sql, valores)
        self.conn.commit()
        
    def delete(self, id_):
        pass
    
    def select(self):
        pass


