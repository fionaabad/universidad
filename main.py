import mysql.connector
from carrera import Carrera
from DAOcarrera import CarreraDAO

def mostrar_menu():
    menu = ("\033[33m1.- Añadir.\n"
        "2.- Actualizar.\n"
        "3.- Ver.\n"
        "4.- Borrar.\n"
        "0.- Apagar programa.\033[0m\n"
    )
    return menu

def opcion_crear(dao, nombre, duracion):
    c = Carrera(nombre, duracion)
    dao.create(c)

def opcion_ver(dao, id_ = -1):
    pass

def opcion_actualizar(dao, id_, nombre, duracion):
    ok = dao.update(Carrera(nombre, duracion, id_))
    if ok:
        return("Carrera actualizada.")
    else:
        return("No se encontró la carrera.")
        
def opcion_borrar(dao, nombre):
    ok = dao.delete(Carrera(nombre))
    if ok:
        return("Carrera eliminada.")
    else:
        return("No se encontró la carrera.")

    

