import mysql.connector
import json

#DICCIONARIO DE BATALLAS
# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='1234',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
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
        print("Opciones:")
        print("1. Mostrar ranking")
        print("2. Actualizar puntuación de un jugador")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            mostrar_ranking()
            break

        elif opcion == '2':
            jugador = input("Ingresa el nombre del jugador: ")
            nueva_puntuacion = int(input("Ingresa la nueva puntuación: "))
            actualizar_puntuacion(jugador, nueva_puntuacion)
            break
        elif opcion == '3':
            print("Saliendo de la consola...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Función para actualizar la puntuación de un jugador
def actualizar_puntuacion(jugador, nueva_puntuacion):
    if jugador in jugadores:
        jugadores[jugador] = nueva_puntuacion
        print(f"Puntuación de {jugador} actualizada a {nueva_puntuacion}.")
    else:
        print(f"El jugador {jugador} no existe en el ranking.")

# Función para obtener el ranking global
def obtener_ranking():
    # Ordenamos los jugadores por puntuación de forma descendente
    ranking = sorted(jugadores.items(), key=lambda x: x[1], reverse=True)
    return ranking

# Función para mostrar el ranking
def mostrar_ranking():
    ranking_global = obtener_ranking()
    print("\nRanking Global:")
    for i, (jugador, puntuacion) in enumerate(ranking_global, start=1):
        print(f"{i}. {jugador}: {puntuacion} puntos")
    print()  # Línea en blanco para mejor legibilidad

if __name__ == "__main__":
    ranking()