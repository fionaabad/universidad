import mysql.connector
from carrera import Carrera

class CarreraDAO:
    def __init__(self):
        self.SetConn(mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="universidad") )
        self.SetCursor(self.__conn.cursor()) 

    def GetConn(self):
        return self.__conn
    
    def SetConn(self, conn):
        self.__conn = conn
        
    def GetCursor(self):
        return self.__cursor
    
    def SetCursor(self, cursor):
        cursor
        self.__cursor = cursor 

    def create(self, c):
        sql = "INSERT INTO carreras (nombre, duracion, id) VALUES (%s, %s, %s)"
        self.GetCursor().execute(sql, (c.nombre, c.duracion, c.id_))
        self.GetConn().commit()
        self.GetCursor().close()
    
    def read(self, nombre = ""):
        query = ""

        if nombre == "":
            query = "SELECT * FROM carrera"
            self.GetCursor().execute(query)

        else:
            query = "SELECT * FROM carrera WHERE nombre LIKE %s"
            values = [nombre]
            self.GetCursor().execute(query, values)
            
        return self.GetCursor().fetchall()
    
    def update(self, c):
        sql = "UPDATE carrera SET nombre = %s, duracion = %s WHERE id = %s"
        valores = (c.GetNombre(), c.GetDuracion(), c.GetId())
        self.GetCursor().execute(sql, valores)
        self.GetConn.commit()
        
    def delete(self, id_):
        sql = "DELETE FROM carreras WHERE id = %s"
        self.GetCursor().execute(sql, (id_,))
        self.GetConn().commit()
