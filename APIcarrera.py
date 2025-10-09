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

app = Flask(__name__)
      
class APIcarrera:
    
    @app.route("/create/", methods = ["POST"])
    def create():
        data = req.get_json()
        
        nombre = data['nombre']
        duracion = data['duracion']
        crear_carrera = Carrera(nombre, duracion)
        CarreraDAO.create(crear_carrera, conn)
        return jsonify({'mensaje': 'Carrera creada correctamente.'})
    
    @app.route("/update/", methods = ["PUT"])
    def update():
        return "placeholder"
    
    @app.route("/read/", methods = ["GET"])
    def read():
        return "placeholder"
    
    @app.route("/delete/", methods = ["DELETE"])
    def delete():
        data = req.get_json()
        nombre = data['nombre']
        borrar_carrera = Carrera(nombre)
        CarreraDAO.delete(borrar_carrera, conn)
        
        return jsonify({'mensaje': 'Carrera eliminada correctamente.'})