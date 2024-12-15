import mysql.connector
#import json

db = mysql.connector.connect(user='root',password='12345',host='localhost',database="Videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

# CRUD
def RegistrarJugador():
    if db:
        try:
            cursor = db.cursor()
            jug_nombre = input("Nombre: ")
            nivel = int(input("Nivel: "))
            puntuacion = int(input("Puntuación: "))
            equipo = input("Equipo: ")
            inventario = input("Inventario:")
            cursor.callproc('RegistraJugador', [jug_nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("Jugador registrado.")
        finally:
            cursor.close()
            db.close()

# Consultar jugadores
def ConsultarJugadores():
    if db:
        try:
            cursor = db.cursor()
            cursor.callproc('ConsultarJugadores')
            for result in cursor.stored_results():
                jugadores = result.fetchall()
                for jugador in jugadores:
                    print(jugador)
        finally:
                cursor.close()
                db.close()

# Modificar jugador
def ModificadorJugadores():
    if db:
        try:
            cursor = db.cursor()
            id_jugador = int(input("ID del jugador: "))
            nombre = input("Nuevo nombre: ")
            nivel = int(input("Nuevo nivel: "))
            puntuacion = int(input("Nueva puntuacion: "))
            equipo = input("Nuevo equipo: ")
            inventario = input("Nuevo inventario: ")
            cursor.callproc('ModificarJugador', [id_jugador, nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("Jugador modificado.")
        finally:
            cursor.close()
            db.close()

# Eliminar jugador
def EliminarJugador():
    if db:
        try:
            cursor = db.cursor()
            id_jugador = int(input("ID del jugador: "))
            cursor.callproc('EliminarJugador', [id_jugador])
            db.commit()
            print("Jugador eliminado.")
        finally:
            cursor.close()
            db.close()

# Menú principal
def menu():
    while True:
        print("\n**** REGISTRAR JUGADORES ****\n")
        print("1. Registarar a un jugador")
        print("2. Consultar a los jugadores")
        print("3. Modificar a un jugador")
        print("4. Eliminar a un jugador")
        print("5. Salir")
        opcion = input("\nPor favor eliga una opcion para poder continuar: ")

        if opcion == "1":
            RegistrarJugador()
            break
        elif opcion == "2":
            ConsultarJugadores()
            break
        elif opcion == "3":
            ModificadorJugadores()
            break
        elif opcion == "4":
            EliminarJugador()
            break
        elif opcion == "5":
            print("Cerrando Registros........")
        else:
            print("ESTA OPCIÓN NO ES VÁLIDA")

# Ejecutar el menú
if __name__ == "__main__":
    menu()