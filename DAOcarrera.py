import mysql.connector
from carrera import Carrera

class CarreraDAO:
    def __init__(self, conn):
        self.__conn = conn
        
    def create(self, c):
        pass
    
    def read(self, nombre = ""):
        query = ""

        if nombre == "":
            query = "SELECT * FROM carrera"
            GetCursor().execute(query)

        else:
            query = "SELECT * FROM carrera WHERE nombre LIKE %s"
            values = [nombre]
            GetCursor().execute(query, values)
            
        return GetCursor().fetchall()
    
    def update(self, c):
        pass
    
    def delete(self, id_):
        pass
    
    def select(self):
        pass


