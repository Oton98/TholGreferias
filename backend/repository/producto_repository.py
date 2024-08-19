from backend.database import DatabaseConnection
from backend.models.product import Producto
from backend.shared import logger

class ProductoRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ProductoRepository, cls).__new__(cls)
            cls._instance.__init_singleton(*args, **kwargs)
        return cls._instance

    def __init_singleton(self, *args, **kwargs):
        self.db_connection = DatabaseConnection().connect()
        self.logger = logger
        
    def get_all(self, include_unavailable=False):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto" if include_unavailable else "SELECT * FROM producto WHERE estaDisponible = TRUE"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]

    def get_by_id(self, producto_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE id = %s"
        cursor.execute(query, (producto_id,))
        result = cursor.fetchone()
        cursor.close()
        return Producto(*result) if result else None

    def get_by_type(self, tipo):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE tipo = %s"
        cursor.execute(query, (tipo,))
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]
    
    def get_by_type_like(self, tipo):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE tipo like %s"
        cursor.execute(query, (tipo,))
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]


    def get_destacados(self):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE esDestacado = TRUE"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]
    
    def count_destacados(self):
        cursor = self.db_connection.cursor()
        query = "SELECT COUNT(*) FROM producto WHERE esDestacado = TRUE"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def get_by_coleccion(self, coleccion_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE coleccion_id = %s "
        cursor.execute(query, (coleccion_id))
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]

    def get_by_coleccion_and_type(self, coleccion_id, tipo):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE coleccion_id = %s AND tipo = %s"
        cursor.execute(query, (coleccion_id, tipo))
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]
    
    def get_by_coleccion_and_type_and_allowed(self, coleccion_id, tipo):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE coleccion_id = %s AND tipo = %s AND estaDisponible = TRUE"
        cursor.execute(query, (coleccion_id, tipo))
        result = cursor.fetchall()
        cursor.close()
        return [Producto(*row) for row in result]

    def get_by_coleccion_type_and_id(self, coleccion_id, tipo, producto_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM producto WHERE coleccion_id = %s AND tipo = %s AND id = %s"
        cursor.execute(query, (coleccion_id, tipo, producto_id))
        result = cursor.fetchone()
        cursor.close()
        return Producto(*result) if result else None

    def create(self, producto):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO producto (nombre, tipo, codigo, descripcion, imagen, colores, manual, medidas, 
                                  estaDisponible, esDestacado, coleccion_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (producto.nombre, producto.tipo, producto.codigo, producto.descripcion, 
                                   producto.imagen, producto.colores, producto.manual, producto.medidas, 
                                   producto.esta_disponible, producto.es_destacado, producto.coleccion_id))
            self.db_connection.commit()
            self.logger.info("Producto created successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error creating producto: {e}")
        finally:
            cursor.close()

    def update(self, producto_id, producto):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE producto 
            SET nombre=%s, tipo=%s, codigo=%s, descripcion=%s, imagen=%s, colores=%s, manual=%s, 
                medidas=%s, estaDisponible=%s, esDestacado=%s, coleccion_id=%s 
            WHERE id=%s
        """
        try:
            cursor.execute(query, (producto.nombre, producto.tipo, producto.codigo, producto.descripcion, 
                                   producto.imagen, producto.colores, producto.manual, producto.medidas, 
                                   producto.esta_disponible, producto.es_destacado, producto.coleccion_id, producto_id))
            self.db_connection.commit()
            self.logger.info("Producto updated successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error updating producto: {e}")
        finally:
            cursor.close()

    def delete(self, producto_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM producto WHERE id = %s"
        try:
            cursor.execute(query, (producto_id,))
            self.db_connection.commit()
            self.logger.info("Producto deleted successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error deleting producto: {e}")
        finally:
            cursor.close()
            
    def delete_by_coleccion_id(self, coleccion_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM producto WHERE coleccion_id = %s"
        try:
            cursor.execute(query, (coleccion_id,))
            self.db_connection.commit()
            self.logger.info("Productos deleted successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error deleting productos: {e}")
        finally:
            cursor.close()