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
    ok = dao.create(c)
    if ok:
        return True
    else:
        return False

def opcion_ver(dao, nombre = ""):
    return dao.read(nombre)

def opcion_actualizar(dao, id_, nombre, duracion):
    ok = dao.update(Carrera(nombre, duracion, id_))
    if ok:
        return True
    else:
        return False
        
def opcion_borrar(dao, nombre):
    ok = dao.delete(Carrera(nombre))
    if ok:
        return True
    else:
        return False

    
dao = CarreraDAO()   

while True:
    print(mostrar_menu())
    opcion = input("Elige opción: ").strip()
    
    if opcion == "1":
        pass
    
    elif opcion == "2":
        pass
    
    elif opcion == "3":
        pass
    
    elif opcion == "4":
        pass
    
    elif opcion == '0':
        pass
    
    else:
        print("Opción no válida")


    
    
