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
    
    def read(self, id_):
        pass
    
    def update(self, c):
        pass
    
    def delete(self, id_):
        pass
    
    def fetchall(self):
        pass


