import mysql.connector
from carrera import Carrera

class CarreraDAO:

    def create(self, c):
        sql = "INSERT INTO carreras (nombre, duracion) VALUES (%s, %s)"
        self.GetCursor().execute(sql, (c.GetNombre(), c.GetDuracion()))
        self.GetConn().commit()


    def update(self, c, nombre_original):
        sql = "UPDATE carreras SET nombre = %s, duracion = %s WHERE nombre = %s"
        valores = (c.GetNombre(), c.GetDuracion(), nombre_original)
        self.GetCursor().execute(sql, valores,)
        self.GetConn().commit()
        
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
            duracion_carrera = round(float(registro[2]), 1)

            carrera = Carrera(nombre_carrera, duracion_carrera, id_carrera)
            carreras.append(carrera)
        return carreras
        
    def delete(self, nombre):
        sql = "DELETE FROM carreras WHERE nombre = %s"
        self.GetCursor().execute(sql, (nombre,))
        self.GetConn().commit()
