import mysql.connector
from carrera import Carrera

class CarreraDAO:


    def create(c, conn):
        sql = "INSERT INTO carreras (nombre, duracion) VALUES (%s, %s)"
        conn.GetCursor().execute(sql, (c.GetNombre(), c.GetDuracion()))
        conn.GetConn().commit()


    def update(c, conn):
        sql = "UPDATE carreras SET nombre = %s, duracion = %s WHERE nombre = %s"
        valores = (c.GetNombre(), c.GetDuracion(), nombre_original)
        conn.GetCursor().execute(sql, valores,)
        conn.GetConn().commit()
        
    def read(conn, nombre = ""):
        query = ""

        if nombre == "":
            query = "SELECT * FROM carreras"
            conn.GetCursor().execute(query)

        else:
            fnombre = f"%{nombre}%"
            query = "SELECT * FROM carreras WHERE nombre LIKE %s"
            conn.GetCursor().execute(query, (fnombre,))
            
        registros = conn.GetCursor().fetchall()
        carreras = []
        for registro in registros:
            id_carrera = registro[0]
            nombre_carrera = registro[1]
            duracion_carrera = round(float(registro[2]), 1)

            carrera = Carrera(nombre_carrera, duracion_carrera, id_carrera)
            carreras.append(carrera)
        return carreras
        
    def delete(nombre, conn):
        sql = "DELETE FROM carreras WHERE nombre = %s"
        conn.GetCursor().execute(sql, (nombre,))
        conn.GetConn().commit()
