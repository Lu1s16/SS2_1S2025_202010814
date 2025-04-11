
CREATE DATABASE seminario2_202010814;


USE seminario2_202010814
GO

CREATE TABLE Proveedor (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    CodProveedor VARCHAR(10),
    Nombre VARCHAR(100),
    Direccion VARCHAR(150),
    Numero INT,
    Web CHAR(1) -- 'S' o 'N'
);
GO

CREATE TABLE Fecha (
    ID INT IDENTITY(1,1) PRIMARY KEY,
	Fecha Date,
    Anio INT,
    Mes INT,
    Dia INT
);
GO

CREATE TABLE Sucursal (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    CodSucursal VARCHAR(10),
    Nombre VARCHAR(100),
    Direccion VARCHAR(150),
    Region VARCHAR(50),
    Departamento VARCHAR(50)
);
GO

CREATE TABLE Producto (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    CodProducto VARCHAR(10),
    Nombre VARCHAR(100),
    Marca VARCHAR(100),
    Categoria VARCHAR(50)
);
GO

CREATE TABLE Cliente (
    ID INT IDENTITY(1,1) PRIMARY KEY,
	CodCliente VARCHAR(10),
    Nombre VARCHAR(100),
    Tipo VARCHAR(15),
    Direccion VARCHAR(150),
    Numero INT
);
GO

CREATE TABLE Vendedor (
    ID INT IDENTITY(1,1) PRIMARY KEY,
	CodVendedor VARCHAR(10),
    Nombre VARCHAR(100),
    Vacacionista VARCHAR(1) -- '1' o '0'
);
GO

CREATE TABLE Compra (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Fecha INT,
    Proveedor INT,
    Producto INT,
    Sucursal INT,
    Unidades INT,
    CostoU DECIMAL(10, 2),
    FOREIGN KEY (Fecha) REFERENCES Fecha(ID),
    FOREIGN KEY (Proveedor) REFERENCES Proveedor(ID),
    FOREIGN KEY (Producto) REFERENCES Producto(ID),
    FOREIGN KEY (Sucursal) REFERENCES Sucursal(ID)
);
GO

CREATE TABLE Venta (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Fecha INT,
    Cliente INT,
    Vendedor INT,
    Producto INT,
    Sucursal INT,
    Unidades INT,
    CostoU DECIMAL(10, 2),
    FOREIGN KEY (Fecha) REFERENCES Fecha(ID),
    FOREIGN KEY (Cliente) REFERENCES Cliente(ID),
    FOREIGN KEY (Vendedor) REFERENCES Vendedor(ID),
    FOREIGN KEY (Producto) REFERENCES Producto(ID),
    FOREIGN KEY (Sucursal) REFERENCES Sucursal(ID)
);
GO

SELECT * FROM Sucursal;
SELECT * FROM Sucursal;
SELECT * FROM Producto;
SELECT * FROM Compra;
SELECT * FROM Venta;