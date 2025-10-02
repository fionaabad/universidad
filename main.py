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

def opcion_crear(dao):
    nombre = input("Nombre de la carrera: ")
    duracion = int(input("Duración en años: "))
    c = Carrera(nombre, duracion)
    dao.create(c)     

def opcion_ver(dao, id_ = -1):
    pass
    
def opcion_actualizar(dao):
    id_ = int(input("ID a actualizar: "))
    nombre = input("Nuevo nombre: ").strip()
    duracion = int(input("Nueva duración (años): "))
    ok = dao.update(Carrera(nombre, duracion, id_))
    if ok:
        print("Carrera actualizada.")
    else:
        print("No se encontró la carrera.")
        
def opcion_borrar(dao):
    pass

    

