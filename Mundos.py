#GRAFO
import mysql.connector
import json

# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='12345',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()
class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista) NODO: UBICACION JUGADORES ARISTA: RUTA Y EL PESO ES LA DISTANCIA
    def add_edge(self, ubicacion, rutas, distancia=1):
        if ubicacion not in self.graph:
            self.graph[ubicacion] = []
        self.graph[ubicacion].append((rutas, distancia))

    # Consultar mundos
    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for ubicacion in self.graph:
            for rutas, distancia in self.graph[ubicacion]:
                edges.append((ubicacion, rutas, distancia))
        return edges

    # Actualizar mundo
    def update_edge(self, ubicacion1, ubicacion2, nueva_distancia):
        if ubicacion1 in self.graph and ubicacion2 in self.graph:
            for i, (rutas) in enumerate(self.graph[ubicacion1]):
                if rutas == ubicacion2:
                    self.graph[ubicacion1][i] = (ubicacion2, nueva_distancia)
                    return True
        return False

    # Eliminar mundo
    def delete_node(self, ubicacion):
        if ubicacion in self.graph:
            del self.graph[ubicacion]
            for u in self.graph:
                self.graph[u] = [(rutas, distancia) for rutas, distancia in self.graph[u] if rutas != ubicacion]
            return True
        return False

# Ejemplo de uso
graph = Graph()
graph.graph = {
    '1': {'2': 100, '3': 700, '5': 300},
    '2': {'1': 100, '3': 200, '5': 600},
    '3': {'1': 700, '2': 200, '4': 150, '5': 550},
    '4': {'3': 150, '5': 500},
    '5': {'1': 300, '2': 600, '3': 550, '4': 500},
}
# Crear una instancia del grafo
graph = Graph()

# Agregar rutas ( ubicació y rutas)
graph.add_edge('1', '2', 100)
graph.add_edge('1', '3', 700)
graph.add_edge('1', '5', 300)
graph.add_edge('2', '3', 200)
graph.add_edge('2', '5', 600)
graph.add_edge('3', '4', 150)
graph.add_edge('3', '5', 550)
graph.add_edge('4', '5', 500)

# Consultar Ubicaciones
print("Ubicación en el grafo:", graph.get_nodes())

# Consultar rutas
print("Ruta en el grafo:", graph.get_edges())

# Actualizar la distancia entre dos Ubicaciones
print("Actualizando la distancia entre 1 y 2 a 150...")
graph.update_edge('1', '2', 150)

# Eliminar una ubicación
print("Eliminando la ubicación 3...")
graph.delete_node('3')

# Consultar después de la eliminación
print("Ubicación después de la eliminación:", graph.get_nodes())
print("Ruta después de la eliminación:", graph.get_edges())