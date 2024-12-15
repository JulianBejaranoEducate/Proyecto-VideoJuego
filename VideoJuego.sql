CREATE DATABASE Videojuego;
USE Videojuego;

CREATE TABLE jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    nivel INT NOT NULL DEFAULT 1,
    puntuacion INT NOT NULL DEFAULT 0,
    equipo VARCHAR(50) NULL,
    inventario TEXT
);

CREATE TABLE partidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    equipo1 VARCHAR(50) NOT NULL,
    equipo2 VARCHAR(50) NOT NULL,
    resultado VARCHAR(50) NOT NULL
);

CREATE TABLE mundos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grafo_serializado TEXT NOT NULL
);

CREATE TABLE ranking (
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_jugador INT NOT NULL,
    puntuacion INT NOT NULL,
    posicion INT UNIQUE,
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id)
);

-- SELECCIONA EL TOP 10 DE MAYOR PUNTUACIÓN 
SELECT nombre, puntuacion 
FROM jugadores
ORDER BY puntuacion DESC
LIMIT 10;

-- PROCEDIMIENTOS DE ALMACENAMIENTO PARA JUGADOR

DELIMITER //
CREATE PROCEDURE RegistrarJugador(
    IN p_nombre VARCHAR(100), 
    IN p_nivel INT, 
    IN p_puntuacion INT, 
    IN p_equipo VARCHAR(50), 
    IN p_inventario TEXT
)
BEGIN
    INSERT INTO jugadores (nombre, nivel, puntuacion, equipo, inventario)
    VALUES (p_nombre, p_nivel, p_puntuacion, p_equipo, p_inventario);
END //
DELIMITER ;

CALL RegistrarJugador('Natalia', 5, 10, 'Equipo2', '{"Arco": 4, "Armadura": 3}');

DELIMITER //
CREATE PROCEDURE ConsultarJugadores()
BEGIN
    SELECT * FROM jugadores;
END //
DELIMITER ;

CALL ConsultarJugadores();

DELIMITER //
CREATE PROCEDURE ModificarJugador(
    IN p_id INT, 
    IN p_nombre VARCHAR(100), 
    IN p_nivel INT, 
    IN p_puntuacion INT, 
    IN p_equipo VARCHAR(50), 
    IN p_inventario TEXT
)
BEGIN
    UPDATE jugadores
    SET nombre = p_nombre, nivel = p_nivel, puntuacion = p_puntuacion, equipo = p_equipo, inventario = p_inventario
    WHERE id = p_id;
END //
DELIMITER ;

CALL ModificarJugador(1, 'Julian', 5, 200, 'Equipo1', '{"Armadura": 3, "Arco": 4}');

DELIMITER //
CREATE PROCEDURE EliminarJugador(IN p_id INT)
BEGIN
    DELETE FROM jugadores
    WHERE id = p_id;
END //
DELIMITER ;

CALL EliminarJugador(21);

-- PROCEDIMIENTOS DE ALMACENAMIENTO MUNDOS

DELIMITER //
CREATE PROCEDURE InsertarMundo(IN p_grafo_serializado TEXT)
BEGIN
    INSERT INTO mundos (grafo_serializado) VALUES (p_grafo_serializado);
END //
DELIMITER ;

CALL InsertarMundo('{"nodos": ["A", "B"], "aristas": [["A", "B"]]}');

DELIMITER //
CREATE PROCEDURE ActualizarMundo(IN p_id INT, IN p_grafo_serializado TEXT)
BEGIN
    UPDATE mundos
    SET grafo_serializado = p_grafo_serializado
    WHERE id = p_id;
END //
DELIMITER ;

CALL ActualizarMundo(1, '{"nodos": ["A", "B", "C"], "aristas": [["A", "B"], ["B", "C"]]}');

DELIMITER //
CREATE PROCEDURE ConsultarMundo(IN p_id INT)
BEGIN
    SELECT * FROM mundos WHERE id = p_id;
END //
DELIMITER ;

CALL ConsultarMundo(2);

DELIMITER //
CREATE PROCEDURE EliminarMundo(IN p_id INT)
BEGIN
    DELETE FROM mundos WHERE id = p_id;
END //
DELIMITER ;

CALL EliminarMundo(1);

DELIMITER //
CREATE PROCEDURE ConsultarUbicaciones()
BEGIN
    SELECT id, grafo_serializado AS ubicaciones
    FROM mundos;
END //
DELIMITER ;

CALL ConsultarUbicaciones();

DELIMITER //
CREATE PROCEDURE EliminarUbicacion(IN p_id INT, IN p_ubicacion VARCHAR(50))
BEGIN
    -- Eliminar el nodo
    UPDATE mundos
    SET grafo_serializado = grafo_serializado
    WHERE id = p_id;

    -- Eliminar las rutas asociadas
    UPDATE mundos
    SET grafo_serializado = grafo_serializado
    WHERE id = p_id;
END //
DELIMITER ;

CALL EliminarUbicacion(1, 'A');

DELIMITER //
CREATE PROCEDURE AgregarRuta(IN p_id INT, IN p_ruta TEXT)
BEGIN
    UPDATE mundos
    SET grafo_serializado = CONCAT(grafo_serializado, ',', p_ruta)
    WHERE id = p_id;
END //
DELIMITER ;

CALL AgregarRuta(1, '{"origen": "A", "destino": "B", "distancia": 10}');

DELIMITER //
CREATE PROCEDURE ConsultarRutas()
BEGIN
    SELECT id, grafo_serializado AS rutas
    FROM mundos;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarDistancia(IN p_id INT, IN p_ruta TEXT, IN p_distancia INT)
BEGIN
    UPDATE mundos
    SET grafo_serializado = grafo_serializado
    WHERE id = p_id;
END //
DELIMITER ;

-- PROCEDIMIENTOS DE ALMACENAMIENTO PARTIDAS

DELIMITER //
CREATE PROCEDURE InsertarPartida(
    IN p_fecha DATETIME, 
    IN p_equipo1 VARCHAR(50), 
    IN p_equipo2 VARCHAR(50), 
    IN p_resultado VARCHAR(50)
)
BEGIN
    INSERT INTO partidas (fecha, equipo1, equipo2, resultado)
    VALUES (p_fecha, p_equipo1, p_equipo2, p_resultado);
END //
DELIMITER ;

CALL InsertarPartida('2024-12-13', 'Equipo A', 'Equipo B', '2-1');

DELIMITER //
CREATE PROCEDURE ConsultarPartidas()
BEGIN
    SELECT * FROM partidas;
END //
DELIMITER ;

CALL ConsultarPartidas();

DELIMITER //
CREATE PROCEDURE ActualizarPartida(
    IN p_id INT, 
    IN p_fecha DATETIME, 
    IN p_equipo1 VARCHAR(50), 
    IN p_equipo2 VARCHAR(50), 
    IN p_resultado VARCHAR(50)
)
BEGIN
    UPDATE partidas
    SET fecha = p_fecha, equipo1 = p_equipo1, equipo2 = p_equipo2, resultado = p_resultado
    WHERE id = p_id;
END //
DELIMITER ;

CALL ActualizarPartida(1, '2024-12-14', 'Equipo C', 'Equipo D', '3-2');

DELIMITER //
CREATE PROCEDURE EliminarPartida(IN p_id INT)
BEGIN
    DELETE FROM partidas
    WHERE id = p_id;
END //
DELIMITER ;

CALL EliminarPartida(1);

-- PROCEDIMIENTOS DE ALMACENAMIENTO RANKING

DELIMITER //
CREATE PROCEDURE ActualizarRanking(
    IN p_id INT, 
    IN p_puntuacion INT, 
    IN p_posicion INT
)
BEGIN
    UPDATE ranking
    SET puntuacion = p_puntuacion, posicion = p_posicion
    WHERE id = p_id;
END //
DELIMITER ;

CALL ActualizarRanking(1, 1500, 2);

DELIMITER //
CREATE PROCEDURE EliminarRanking(IN p_id INT)
BEGIN
    DELETE FROM ranking
    WHERE id = p_id;
END //
DELIMITER ;

CALL EliminarRanking(1);