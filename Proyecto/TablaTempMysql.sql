CREATE DATABASE IF NOT EXISTS ss2_202010814_pr1;

USE ss2_202010814_pr1;

CREATE TABLE temporal_compras (
    Fecha VARCHAR(15),
    CodProveedor VARCHAR(10),
    NombreProveedor VARCHAR(100),
    DireccionProveedor VARCHAR(150),
    NumeroProveedor VARCHAR(15),
    WebProveedor VARCHAR(10),  -- 'S' o 'N'
    CodProducto VARCHAR(10),
    NombreProducto VARCHAR(100),
    MarcaProducto VARCHAR(100),
    Categoria VARCHAR(50),
    CodSucursal VARCHAR(10),
    NombreSucursal VARCHAR(100),
    DireccionSucursal VARCHAR(150),
    Region VARCHAR(50),
    Departamento VARCHAR(50),
    Unidades VARCHAR(6),
    CostoU VARCHAR(15)
);

CREATE TABLE temporal_ventas (
    Fecha VARCHAR(15),
    CodigoCliente VARCHAR(10),
    NombreCliente VARCHAR(100),
    TipoCliente VARCHAR(15),
    DireccionCliente VARCHAR(150),
    NumeroCliente VARCHAR(15),
    CodVendedor VARCHAR(10),
    NombreVendedor VARCHAR(100),
    Vacacionista VARCHAR(10), -- '1' o '0'
    CodProducto VARCHAR(10),
    NombreProducto VARCHAR(100),
    MarcaProducto VARCHAR(100),
    Categoria VARCHAR(50),
    CodSucursal VARCHAR(10),
    NombreSucursal VARCHAR(100),
    DireccionSucursal VARCHAR(150),
    Region VARCHAR(50),
    Departamento VARCHAR(50),
    Unidades VARCHAR(6),
    PrecioUnitario VARCHAR(15)
);