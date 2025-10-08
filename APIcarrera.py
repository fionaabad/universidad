from carrera import Carrera
from DAOcarrera import CarreraDAO
from flask import Flask, jsonify, request as req

class APIcarrera:

    app = Flask(__name__)

    @app.route("/create/", methods = "POST")
    def create():
        return "placeholder"
    
    @app.route("/update/", methods = "PUT")
    def update():
        return "placeholder"
    
    @app.route("/read/", methods = "GET")
    def read():
        return "placeholder"
    
    @app.route("/delete/", methods = "DELETE")
    def delete():
        return "placeholder"