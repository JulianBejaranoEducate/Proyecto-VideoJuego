#TABLAS HASH
import mysql.connector
import json

#TABLA HASH
# CONECTAMOS LA BASE DE DATOS
db = mysql.connector.connect(user='root',password='12345',host='localhost',database="videojuego", auth_plugin="mysql_native_password")
cursor = db.cursor()

class HashTable:
    def __init__(self, size=4):
        """Inicializa la tabla hash con un tamaño fijo."""
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Cada índice almacena una lista para manejar colisiones.

    def _hash(self, key):
        
        """Función hash personalizada: convierte el número de matrícula en un índice."""
        #print(f"Clave '{key}' mapeada al índice {hashed} usando la funcion hash personalizada")

        hashed=  hash(key) % self.size
        print(f"Clave '{key}' mapeada al índice {hashed} usando la funcion hash")
        
        return hashed    
    

    def insert(self, key, value):
        """Inserta un estudiante en la tabla hash."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Actualiza si la clave ya existe.
                return
        self.table[index].append([key, value])  # Inserta una nueva entrada.

    def search(self, key):
        """Busca un inventario de jugador."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Devuelve los datos del estudiante.
        return None  # No se encontró.

    def delete(self, key):
        """Elimina el inventario de un jugador de la tabla hash."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True  # Elimina y confirma.
        return False  # No se encontró para eliminar.

    def display(self):
        """Muestra el contenido de la tabla hash."""
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tabla hash para estudiantes
    inventario = HashTable(size=5)

    # Insertar inventario
    inventario.insert("Inventario", {"Escudo":1,"Espada":2,"Armadura":3,"Arco":4})

    # Mostrar la tabla hash
    print("Tabla hash inicial:")
    inventario.display()


    # Mostrar la tabla hash después de eliminar
    print("\nTabla hash después de eliminar:")
    
    print(hash(42))         # Devuelve 42
    print(hash("Python"))   # Devuelve un número entero único
    print(hash((1, 2, 3)))  # Devuelve un hash basado en los elem
    inventario.display()