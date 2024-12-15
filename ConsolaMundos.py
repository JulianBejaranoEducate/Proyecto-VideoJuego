import mysql.connector
import json

# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root', password='12345', host='localhost', database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, ubicacion, rutas, distancia=1):
        if ubicacion not in self.graph:
            self.graph[ubicacion] = []
        self.graph[ubicacion].append((rutas, distancia))

    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for ubicacion in self.graph:
            for rutas, distancia in self.graph[ubicacion]:
                edges.append((ubicacion, rutas, distancia))
        return edges

    def update_edge(self, ubicacion1, ubicacion2, nueva_distancia):
        if ubicacion1 in self.graph and ubicacion2 in self.graph:
            for i, (rutas, distancia) in enumerate(self.graph[ubicacion1]):
                if rutas == ubicacion2:
                    self.graph[ubicacion1][i] = (ubicacion2, nueva_distancia)
                    return True
        return False

    def delete_node(self, ubicacion):
        if ubicacion in self.graph:
            del self.graph[ubicacion]
            for u in self.graph:
                self.graph[u] = [(rutas, distancia) for rutas, distancia in self.graph[u] if rutas != ubicacion]
            return True
        return False

# Crear una instancia del grafo
graph = Graph()

# Agregar rutas iniciales
graph.add_edge('1', '2', 100)
graph.add_edge('1', '3', 700)
graph.add_edge('1', '5', 300)
graph.add_edge('2', '3', 200)
graph.add_edge('2', '5', 600)
graph.add_edge('3', '4', 150)
graph.add_edge('3', '5', 550)
graph.add_edge('4', '5', 500)

# Consola interactiva
def main():
    while True:
        print("\nComandos disponibles:")
        print("1. Consultar ubicaciones")
        print("2. Consultar rutas")
        print("3. Agregar ruta")
        print("4. Actualizar distancia")
        print("5. Eliminar ubicación")
        print("6. Salir")
        
        comando = input("Ingrese un comando: ")

        if comando == '1':
            print("Ubicaciones en el grafo:", graph.get_nodes())
        
        elif comando == '2':
            print("Rutas en el grafo:", graph.get_edges())
        
        elif comando == '3':
            ubicacion = input("Ingrese la ubicación: ")
            ruta = input("Ingrese la ruta: ")
            distancia = int(input("Ingrese la distancia: "))
            graph.add_edge(ubicacion, ruta, distancia)
            print(f"Ruta agregada: {ubicacion} -> {ruta} con distancia {distancia}")
        
        elif comando == '4':
            ubicacion1 = input("Ingrese la ubicación 1: ")
            ubicacion2 = input("Ingrese la ubicación 2: ")
            nueva_distancia = int(input("Ingrese la nueva distancia: "))
            if graph.update_edge(ubicacion1, ubicacion2, nueva_distancia):
                print(f"Distancia actualizada entre {ubicacion1} y {ubicacion2} a {nueva_distancia}")
            else:
                print("No se pudo actualizar la distancia. Verifique las ubicaciones.")
        
        elif comando == '5':
            ubicacion = input("Ingrese la ubicación a eliminar: ")
            if graph.delete_node(ubicacion):
                print(f"Ubicación {ubicacion} eliminada.")
            else:
                print("No se pudo eliminar la ubicación. Verifique si existe.")
        
        elif comando == '6':
            print("Saliendo de la consola.")
            break
        
        else:
            print("Comando no reconocido. Intente de nuevo.")

if __name__ == "__main__":
    main()