import mysql.connector
from carrera import Carrera

class CarreraDAO:
    def __init__(self, user = "root", password = "root"):
        self.SetConn(mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
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

    def update(self, c):
        sql = "UPDATE carreras SET nombre = %s, duracion = %s WHERE id = %s"
        valores = (c.GetNombre(), c.GetDuracion(), c.GetId())
        self.GetCursor().execute(sql, valores,)
        self.GetConn.commit()
        
    def read(self, nombre = ""):
        query = ""

        if nombre == "":
            query = "SELECT * FROM carreras"
            self.GetCursor().execute(query)

        else:
            fnombre = f"%{nombre}%"
            query = "SELECT * FROM carreras WHERE nombre LIKE %s"
            self.GetCursor().execute(query, (fnombre,))
            
        registros = self.GetCursor().fetchall()
        carreras = []
        for registro in registros:
            id_carrera = registro[0]
            nombre_carrera = registro[1]
            duracion_carrera = round(float(registro[2]), 2)

            carrera = Carrera(nombre_carrera, duracion_carrera, id_carrera)
            carreras.append(carrera)
        return carreras
        
    def delete(self, nombre):
        sql = "DELETE FROM carreras WHERE nombre = %s"
        self.GetCursor().execute(sql, (nombre,))
        self.GetConn().commit()
