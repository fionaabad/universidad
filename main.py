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

user = input("(Predeterminado: root) Escribe el usuario: ")
if user == "":
    user = "root"

password = input("(Predeterminado: root) Escribe la contraseña: ")
if password == "":
    password = "root"

dao = CarreraDAO(user, password)

continuar = True

while continuar:
    print(mostrar_menu())
    opcion = input("Elige opción: ").strip()
    
    if opcion == "1":
        nombre = input("Nombre de la carrera: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        dur = input("Duración (años, puede ser decimal): ").strip()
        try:
            duracion = float(dur)
        except ValueError:
            print("Duración no válida. Debe ser un número.")
            continue

        try:
            opcion_crear(dao, nombre, duracion)
            print("Carrera añadida correctamente.")
        except Exception as e:
            print(f"Error al añadir: {e}")
    
    elif opcion == "2":
        pass
    
    elif opcion == "3":
        nombre = input("(opcional) Nombre a buscar: ")
        try:
            carreras = opcion_ver(dao, nombre)
        except Exception as e:
            print(f"Error al leer: {e}")
            continue

        if len(carreras) > 0:
            for carrera in carreras:
                print(carrera)
        else:
            print("Sin resultados")

    elif opcion == "4": 
        nombre = input("Nombre de la carrera a borrar: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        confirmar = input(f"¿Seguro que quieres borrar '{nombre}'? (s/N): ").strip().lower()
        if confirmar == "s":
            try:
                opcion_borrar(dao, nombre)
                print("Carrera borrada (si existía).")
            except Exception as e:
                print(f"Error al borrar: {e}")
        else:
            print("Operación cancelada.")
    
    elif opcion == '0':
        continuar = False
    
    else:
        print("Opción no válida")
