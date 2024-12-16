import mysql.connector
import json

# DICCIONARIO DE BATALLAS
db = mysql.connector.connect(user='root',password='12345',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()


def main():
    equipos = {} 

    while True:
        print("\nINGRESE LA OPCION PARA EL SISTEMA DE BATALLAS:")
        print("1. AGREGA JUGADOR")
        print("2. AGREGA EQUIPO")
        print("3. SALIR")
        
        opcion = input("ELIGE UNA ÓPCION: ")


         # AGREGA AL JUGADOR
        if opcion == "1":
            nombre = input("Nombre del jugador: ")
            equipo = input("Equipo del jugador: ")
            estadisticas = {}

        #INGRESAR LA PUNTUACIÓN
            print("Ingresa el Ranking:")
            while True:
                stat = input("Nombre de la estadística: ")
                if not stat:
                    break
                valor = input(f"Valor de {stat}: ")
                try:
                    valor = float(valor) 
                except ValueError:
                    pass
                estadisticas[stat] = valor

            # Agregar jugador al equipo
            if equipo not in equipos:
                equipos[equipo] = []
            equipos[equipo].append({"nombre": nombre, "estadisticas": estadisticas})
            print(f"Jugador {nombre} agregado al equipo {equipo}.")

        elif opcion == "2":
            # Ver equipos
            if not equipos:
                print("No hay equipos registrados.")
            else:
                for equipo, jugadores in equipos.items():
                    print(f"\nEquipo: {equipo}")
                    for jugador in jugadores:
                        print(f"  Jugador: {jugador['nombre']}")
                        print("    Estadísticas:")
                        for stat, valor in jugador['estadisticas'].items():
                            print(f"      {stat}: {valor}")

        elif opcion == "3":
            # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()