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
    return dao.create(nombre, duracion)

def opcion_actualizar(dao, id_, nombre, duracion):
    return dao.update(nombre, duracion, id_)

def opcion_ver(dao, nombre = ""):
    return dao.read(nombre)
       
def opcion_borrar(dao, nombre):
    return dao.delete(nombre)
    
dao = CarreraDAO()   


continuar = True

while continuar:
    print(mostrar_menu())
    opcion = input("Elige opción: ").strip()
    
    if opcion == "1":
        pass
    
    elif opcion == "2":
        pass
    
    elif opcion == "3":
        nombre = input("(opcional) Nombre a buscar: ")
        carreras = opcion_ver(dao, nombre)

        if len(carreras) > 0:
            for carrera in carreras:
                print(carrera)
        else:
            print("Sin resultados")

    
    elif opcion == "4":
        pass
    
    elif opcion == '0':
        continuar = False
    
    else:
        print("Opción no válida")


    
    
