CREATE TABLE Usuario(
    id_usuario INT AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    celular CHAR(10) NOT NULL,
    direccion VARCHAR(50) NOT NULL,
    correo VARCHAR(10) NOT NULL,
    pass_word VARCHAR(20) NOT NULL,
    CONSTRAINT pk_id_usuario PRIMARY KEY(id_usuario),
    CONSTRAINT uq_correo UNIQUE(correo)
);

CREATE TABLE Libro(
	id_libro INT AUTO_INCREMENT,
	titulo VARCHAR(50) NOT NULL,
	autor VARCHAR(50) NOT NULL,
	palabras_claves VARCHAR(100),
	categoria VARCHAR(20) NOT NULL,
	unidades INT NOT NULL,
	valor INT NOT NULL,
	CONSTRAINT pk_id_libro PRIMARY KEY(id_libro)
);

CREATE TABLE LibroDeseo(
	id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    CONSTRAINT pk_libro_deseo PRIMARY KEY(id_usuario, id_libro),
    CONSTRAINT fk_id_libro FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_id_libro FOREIGN KEY(id_libro) REFERENCES libro(id_libro) ON DELETE CASCADE
);

CREATE TABLE Resena(
    id_resena INT AUTO_INCREMENT,
	fecha DATETIME NOT NULL,
    comentario VARCHAR(500) NOT NULL,
    calificacio INT NOT NULL,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    CONSTRAINT pk_id_resena PRIMARY KEY(id_resena),
    CONSTRAINT fk_id_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_id_libro FOREIGN KEY(id_libro) REFERENCES libro(id_libro) ON DELETE CASCADE
);

CREATE TABLE Articulo(
    id_articulo INT AUTO_INCREMENT,
	cantidad INT NOT NULL,
    valor_articulo INT NOT NULL,
    id_libro INT NOT NULL,
    CONSTRAINT pk_id_articulo PRIMARY KEY(id_articulo),
    CONSTRAINT fk_id_libro FOREIGN KEY(id_libro) REFERENCES libro(id_libro) ON DELETE CASCADE
);

CREATE TABLE carro(
	id_carro INT AUTO_INCREMENT,
    valor_total INT NOT NULL,
    id_usuario INT NOT NULL,
    id_articulo INT NOT NULL,
    CONSTRAINT pk_id_carro PRIMARY KEY(id_carro),
    CONSTRAINT fk_id_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_id_articulo FOREIGN KEY(id_articulo) REFERENCES articulo(id_articulo) ON DELETE CASCADE
);

CREATE TABLE Pago(
	id_pago INT AUTO_INCREMENT,
    tipo_pago VARCHAR(15) NOT NULL,
    CONSTRAINT pk_id_pago PRIMARY KEY(id_pago) 
);

CREATE TABLE Pedido(
    id_pedido INT AUTO_INCREMENT,
	fecha DATETIME NOT NULL,
    estado VARCHAR(20) NOT NULL,
    valor_total INT NOT NULL,
    id_usuario INT NOT NULL,
    id_pago INT NOT NULL,
    CONSTRAINT pk_id_pedido PRIMARY KEY(id_pedido),
    CONSTRAINT fk_id_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_id_pago FOREIGN KEY(id_pago) REFERENCES pago(id_pago) ON DELETE CASCADE
);

CREATE TABLE DetallePedido(
	id_pedido INT NOT NULL,
    id_articulo INT NOT NULL,
    CONSTRAINT pk_detalle_pedido PRIMARY KEY(id_pedido, id_articulo),
	CONSTRAINT fk_pedido FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    CONSTRAINT fk_articulo FOREIGN KEY(id_articulo) REFERENCES articulo(id_articulo) ON DELETE CASCADE
);