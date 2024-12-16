import mysql.connector
import json

#DICCIONARIO DE BATALLAS
# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='12345',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()


# Definimos un diccionario con los jugadores y sus puntuaciones
jugadores = {
    "Jeisson": 1500,
    "Natalia": 2000,
    "Sebastian": 1800,
    "Camilo": 2200,
    "Maria": 1700
}

def ranking():
    while True:
        print("\n=========================")
        print("  RANKING DE JUGADORES    ")
        print("=========================")
        print("1. Mostrar ranking")
        print("2. Actualizar puntuación de un jugador")
        print("3. Salir")
        
        opcion = input("Por favor selecciona opcion para continuar: ")
        
        if opcion == '1':
            mostrar_ranking()

        elif opcion == '2':
            jugador = input("Ingresa el nombre del jugador: ")
            nueva_puntuacion = int(input("Ingresa la nueva puntuación: "))
            actualizar_puntuacion(jugador, nueva_puntuacion)

        elif opcion == '3':
            print("Has salido del ranking de jugadores.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def mostrar_ranking():
    ranking_global = obtener_ranking()
    print("\nRanking Global:")
    for i, (jugador, puntuacion) in enumerate(ranking_global, start=1):
        print(f"{i}. {jugador}: {puntuacion} puntos")
    print()  # Línea en blanco para mejor legibilidad

def actualizar_puntuacion(jugador, nueva_puntuacion):
    if jugador in jugadores:
        jugadores[jugador] = nueva_puntuacion
        print(f"Puntuación de {jugador} actualizada a {nueva_puntuacion}.")
    else:
        print(f"El jugador {jugador} no existe en el ranking.")

def obtener_ranking():
    # Ordenamos los jugadores por puntuación de forma descendente
    ranking = sorted(jugadores.items(), key=lambda x: x[1], reverse=True)
    return ranking

if __name__ == "__main__":
    ranking()