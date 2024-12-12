import sqlite3

class Conneccion():
    def __init__(self):
        self.base_datos = 'sistema.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar_con(self):
        self.conexion.commit()
        self.conexion.close()





def crear_tabla():
    conn = Conneccion()
    
    # Definición de las sentencias SQL para crear las tablas
    sql_producto = '''
        CREATE TABLE IF NOT EXISTS Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(150),
            stock INTEGER,
            precio DECIMAL,
            origen VARCHAR(150),
            tipo_producto VARCHAR(150)
        );
    '''

    sql_cliente = '''
        CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(150),
            apellido VARCHAR(50),
            fecha_nacimiento DATE,
            telefono VARCHAR(150)
        );
    '''

    sql_detalle_venta = '''
        CREATE TABLE IF NOT EXISTS detalle_venta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER,
            id_cliente INTEGER,
            id_producto INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
            FOREIGN KEY (id_producto) REFERENCES Producto(id)
        );
    '''

    try:
        # Crear las tablas una por una
        conn.cursor.execute(sql_producto)
        conn.cursor.execute(sql_cliente)
        conn.cursor.execute(sql_detalle_venta)
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        conn.cerrar_con()
              
class Producto():
    def __init__(self,nombre,stock,precio):
       self.nombre = nombre
       self.stock = stock
       self.precio = precio

    def __str__(self):
        return f'Producto[{self.nombre},{self.stock},{self.precio}]'
    

class Cliente():
    def __init__(self,nombre,apellido,fecha_nacimiento,telefono):
       self.nombre = nombre
       self.apellido = apellido
       self.fecha_nacimiento = fecha_nacimiento
       self.telefono = telefono
    
    
class Detalle_venta():
    def __init__(self,cantidad,id_cliente,id_producto):
       self.cantidad = cantidad
       self.id_cliente = id_cliente
       self.id_producto = id_producto
            
def guardar_producto(producto):
    conn = Conneccion()

    sql= f'''
        INSERT INTO producto(nombre,stock,precio,origen,tipo_producto)
        VALUES('{producto.nombre}','{producto.stock}',{producto.precio},{producto.origen},{producto.tipo_producto});
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_producto():
    conn = Conneccion()
    listar_peliculas = []

    sql= f'''
        SELECT * FROM producto as p;
'''
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except:
        pass


