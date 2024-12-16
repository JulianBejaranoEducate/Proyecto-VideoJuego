import mysql.connector
import json

db = mysql.connector.connect(user='root',password='12345',host='localhost',database="Videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

def menu():
    while True:
        print("\n=========================")
        print("   REGISTRAR JUGADORES    ")
        print("=========================")
        print("1. Registarar a un jugador")
        print("2. Consultar a los jugadores")
        print("3. Modificar a un jugador")
        print("4. Eliminar a un jugador")
        print("5. Salir")
        opcion = input("\nPOR FAVOR ELIJA UNA OPCION PARA CONTINUAR: \n")

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
            print("EL sistema de registro de jugadores ha sido cerrado.")
        else:
            print("ESTA OPCION NO ES VALIDA, INTENTE DE NUEVO.")

def RegistrarJugador():
    if db:
        try:
            cursor = db.cursor()
            nombre = input("Nombre: ")
            nivel = int(input("Nivel: "))
            puntuacion = int(input("Puntuación: "))
            equipo = input("Equipo: ")
            inventario = input("Inventario:")
            cursor.callproc('RegistraJugador', [nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("El jugador ha sido registrado correctamente.")

        finally:
            cursor.close()
            db.close()

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

def ModificadorJugadores():
    if db:
        try:
            cursor = db.cursor()
            id = int(input("ID del jugador: "))
            nombre = input("Nuevo nombre: ")
            nivel = int(input("Nuevo nivel: "))
            puntuacion = int(input("Nueva puntuacion: "))
            equipo = input("Nuevo equipo: ")
            inventario = input("Nuevo inventario: ")
            cursor.callproc('ModificarJugador', [id, nombre, nivel, puntuacion, equipo, inventario])
            db.commit()
            print("El jugador ha sido modificado correctamente.")
        finally:
            cursor.close()
            db.close()

def EliminarJugador():
    if db:
        try:
            cursor = db.cursor()
            id = int(input("ID del jugador: "))
            cursor.callproc('EliminarJugador', [id])
            db.commit()
            print("EL jugador ha sido eliminado correctamente.")
        finally:
            cursor.close()
            db.close()

if __name__ == "__main__":
    menu()