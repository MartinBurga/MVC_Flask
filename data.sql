CREATE TABLE IF NOT EXISTS vendedores (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    fecha_venta DATE NOT NULL,
    vendedor_id INTEGER NOT NULL,
    cuota_monto FLOAT NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores (id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS reglas (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    monto_minimo FLOAT NOT NULL,
    porcentaje_comision FLOAT NOT NULL
) ENGINE=InnoDB;

REPLACE INTO vendedores (id, nombre) VALUES
(1, 'Perico P'),
(2, 'Zoila B'),
(3, 'Aquiles C'),
(4, 'Johny M'),
(5, 'Martin B'),
(6, 'Isabella C');

REPLACE INTO ventas (id, fecha_venta, vendedor_id, cuota_monto) VALUES
(1, '2026-05-21', 1, 400.00),
(2, '2026-05-29', 2, 600.00),
(3, '2026-06-03', 2, 200.00),
(4, '2026-06-09', 1, 300.00),
(5, '2026-06-11', 3, 900.00),
(6, '2026-06-15', 4, 1000.00),
(7, '2026-06-20', 1, 1200.00),
(8, '2026-06-25', 2, 800.00),
(9, '2026-07-01', 3, 500.00),
(10, '2026-07-05', 4, 700.00),
(11, '2026-05-21', 5, 400.00),
(12, '2026-05-12', 6, 600.00);


REPLACE INTO reglas (id, monto_minimo, porcentaje_comision) VALUES
(1, 1000, 1.15),
(2, 800, 0.10),
(3, 600, 0.06),
(4, 500, 0.08);