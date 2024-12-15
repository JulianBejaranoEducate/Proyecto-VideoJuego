import mysql.connector

def conectar_db():
    return mysql.connector.connect(host="localhost", user="root", password="12345", database="Videojuego", auth_plugin="mysql_native_password"
    )

def consultar_ranking_global():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, puntuacion, posicion FROM ranking ORDER BY posicion ASC")
    print("\nRANKING GLOBAL")
    print("Posición | ID del Jugador | Puntuación")
    print("---------------------------------------")
    for id, puntuacion, posicion in cursor.fetchall():
        print(f"{posicion} | {id} | {puntuacion}")
    cursor.close()
    conexion.close()

def actualizar_ranking(id_jugador, nueva_puntuacion, nueva_posicion):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.callproc('ActualizarRanking', [id_jugador, nueva_puntuacion, nueva_posicion])
    conexion.commit()
    print(f"\nRanking del jugador {id_jugador} actualizado correctamente.")
    cursor.close()
    conexion.close()

def menu_ranking():
    while True:
        print("\n=========================")
        print("    RANKING GLOBAL")
        print("=========================")
        print("1. Consultar ranking global")
        print("2. Actualizar ranking de un jugador")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            consultar_ranking_global()
        elif opcion == "2":
            id_jugador = int(input("Ingrese el ID del jugador: "))
            nueva_puntuacion = int(input("Ingrese la nueva puntuación: "))
            nueva_posicion = int(input("Ingrese la nueva posición: "))
            actualizar_ranking(id_jugador, nueva_puntuacion, nueva_posicion)
        elif opcion == "3":
            print("Saliendo del sistema de ranking...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_ranking()
