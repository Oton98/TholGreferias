from backend.database import DatabaseConnection
from backend.models.collection import Coleccion
from backend.shared import logger

class ColeccionRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ColeccionRepository, cls).__new__(cls)
            cls._instance.__init_singleton(*args, **kwargs)
        return cls._instance

    def __init_singleton(self, *args, **kwargs):
        self.db_connection = DatabaseConnection().connect()
        self.logger = logger
    
    def get_all(self, include_deleted=False):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM coleccion" if include_deleted else "SELECT * FROM coleccion WHERE esta_eliminada = FALSE"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return [Coleccion(*row) for row in result]

    def get_by_id(self, coleccion_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM coleccion WHERE id = %s"
        cursor.execute(query, (coleccion_id,))
        result = cursor.fetchone()
        cursor.close()
        return Coleccion(*result) if result else None

    def get_by_name(self, nombre):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM coleccion WHERE nombre = %s AND esta_eliminada = FALSE"
        cursor.execute(query, (nombre,))
        result = cursor.fetchone()
        cursor.close()
        return Coleccion(*result) if result else None

    def create(self, coleccion):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO coleccion (nombre, img_monocomando, img_bimando, img_freestanding, img_accesorio, 
                                   img_complemento, cantidad_productos, esta_eliminada) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (coleccion.nombre, coleccion.img_monocomando, coleccion.img_bimando, 
                                   coleccion.img_freestanding, coleccion.img_accesorio, coleccion.img_complemento, 
                                   coleccion.cantidad_productos, coleccion.esta_eliminada))
            self.db_connection.commit()
            self.logger.info("Coleccion created successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error creating coleccion: {e}")
        finally:
            cursor.close()

    def update(self, coleccion_id, coleccion):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE coleccion 
            SET nombre=%s, img_monocomando=%s, img_bimando=%s, img_freestanding=%s, 
                img_accesorio=%s, img_complemento=%s, cantidad_productos=%s, esta_eliminada=%s 
            WHERE id=%s
        """
        try:
            cursor.execute(query, (coleccion.nombre, coleccion.img_monocomando, coleccion.img_bimando, 
                                   coleccion.img_freestanding, coleccion.img_accesorio, coleccion.img_complemento, 
                                   coleccion.cantidad_productos, coleccion.esta_eliminada, coleccion_id))
            self.db_connection.commit()
            self.logger.info("Coleccion updated successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error updating coleccion: {e}")
        finally:
            cursor.close()

    def delete(self, coleccion_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM coleccion WHERE id = %s"
        try:
            cursor.execute(query, (coleccion_id,))
            self.db_connection.commit()
            self.logger.info("Coleccion deleted successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error deleting coleccion: {e}")
        finally:
            cursor.close()

    def delete_products_by_coleccion_id(self, coleccion_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM producto WHERE coleccion_id = %s"
        try:
            cursor.execute(query, (coleccion_id,))
            self.db_connection.commit()
            self.logger.info("Products deleted successfully for coleccion_id %s", coleccion_id)
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error deleting products: {e}")
        finally:
            cursor.close()