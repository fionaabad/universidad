from carrera import Carrera
from ConexionBD import Conexion
from DAOcarrera import CarreraDAO
from flask import Flask, jsonify, request as req

user = input("(Predeterminado: root) Escribe el usuario: ")
if user == "":
    user = "root"
    
password = input("(Predeterminado: root) Escribe la contraseña: ")
if password == "":
    password = "root"

conn = Conexion(user, password)
      
class APIcarrera:

    app = Flask(__name__)
    
    
    @app.route("/create/", methods = "POST")
    def create():
        data = req.get_json()
        
        nombre = data['nombre']
        duracion = duracion['duracion']
        
        crear_carrera = Carrera(nombre, duracion)
        conn.create(crear_carrera)
        conn.GetConn().close()
        
        return jsonify({'Carrera creada correctamente.'})
    
    @app.route("/update/", methods = "PUT")
    def update():
        return "placeholder"
    
    @app.route("/read/", methods = "GET")
    def read():
        return "placeholder"
    
    @app.route("/delete/", methods = "DELETE")
    def delete():
        data = req.get_json()
        nombre = data['nombre']
        borrar_carrera = Carrera(nombre)
        conn.delete(borrar_carrera)
        conn.GetConn().close()
        
        return jsonify({'Carrera eliminada correctamente.'})