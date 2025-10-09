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

def opcion_crear(dao, carrera):
    return dao.create(carrera)

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
        
        carrera = Carrera(nombre, duracion)

        try:
            crear_carrera = Carrera(nombre, duracion)
            opcion_crear(dao, crear_carrera)
            print("Carrera añadida correctamente.")
        except Exception as e:
            print(f"Error al añadir: {e}")
    
    elif opcion == "2":
        nombre = input("Nombre de la carrera a actualizar: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacio.")
            continue

        carreras = dao.read(nombre)
        if len(carreras) == 0:
            print(f"No se encontró ninguna carrera con el nombre '{nombre}'.")
            continue
        elif len(carreras) > 1:
            print("Hay varias carreras con ese nombre. Especifique un nombre único.")
            for c in carreras:
                print(c)
            continue

        carrera_actual = carreras[0]
        print(f"Carrera encontrada: {carrera_actual}")

        nuevo_nombre = input("Nuevo nombre (dejar vacio para mantener el actual): ").strip()
        if nuevo_nombre == "":
            nuevo_nombre = carrera_actual.GetNombre()

        dur = input("Nueva duración (dejar vacio para mantener la actual): ").strip()
        if dur == "":
            nueva_duracion = carrera_actual.GetDuracion()
        else:
            try:
                nueva_duracion = float(dur)
            except ValueError:
                print("Duración no valida, debe ser un número.")
                continue

       
        carrera_modificada = Carrera(nuevo_nombre, nueva_duracion, carrera_actual.GetId())

        try:
            dao.update(carrera_modificada, carrera_actual.GetNombre())
            print("Carrera actualizada correctamente.")
        except Exception as e:
            print(f"Error al actualizar: {e}")

    
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
