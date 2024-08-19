from backend.database import DatabaseConnection
from backend.models.distribuidores import Distribuidor
from backend.shared import logger

class DistribuidorRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DistribuidorRepository, cls).__new__(cls)
            cls._instance.__init_singleton(*args, **kwargs)
        return cls._instance

    def __init_singleton(self, *args, **kwargs):
        self.db_connection = DatabaseConnection().connect()
        self.logger = logger(self.__class__.__name__)

    def get_all(self, include_deleted=False):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM distribuidor" if include_deleted else "SELECT * FROM distribuidor WHERE esta_eliminado = FALSE"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return [Distribuidor(*row) for row in result]

    def get_by_id(self, distribuidor_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM distribuidor WHERE id = %s"
        cursor.execute(query, (distribuidor_id,))
        result = cursor.fetchone()
        cursor.close()
        return Distribuidor(*result) if result else None

    def create(self, distribuidor):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO distribuidor (nombre, direccion, provincia, latitud, longitud, web, whatsapp, telefono, esta_eliminado) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (distribuidor.nombre, distribuidor.direccion, distribuidor.provincia, 
                                   distribuidor.latitud, distribuidor.longitud, distribuidor.web, 
                                   distribuidor.whatsapp, distribuidor.telefono, distribuidor.esta_eliminado))
            self.db_connection.commit()
            self.logger.info("Distribuidor created successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error creating distribuidor: {e}")
        finally:
            cursor.close()

    def update(self, distribuidor_id, distribuidor):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE distribuidor 
            SET nombre=%s, direccion=%s, provincia=%s, latitud=%s, longitud=%s, web=%s, whatsapp=%s, telefono=%s, esta_eliminado=%s 
            WHERE id=%s
        """
        try:
            cursor.execute(query, (distribuidor.nombre, distribuidor.direccion, distribuidor.provincia, 
                                   distribuidor.latitud, distribuidor.longitud, distribuidor.web, 
                                   distribuidor.whatsapp, distribuidor.telefono, distribuidor.esta_eliminado, distribuidor_id))
            self.db_connection.commit()
            self.logger.info("Distribuidor updated successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error updating distribuidor: {e}")
        finally:
            cursor.close()

    def delete(self, distribuidor_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM distribuidor WHERE id = %s"
        try:
            cursor.execute(query, (distribuidor_id,))
            self.db_connection.commit()
            self.logger.info("Distribuidor deleted successfully")
        except Exception as e:
            self.db_connection.rollback()
            self.logger.error(f"Error deleting distribuidor: {e}")
        finally:
            cursor.close()