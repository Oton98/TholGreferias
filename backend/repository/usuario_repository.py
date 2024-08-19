from backend.database import DatabaseConnection
from backend.models.usuario import Usuario
from backend.shared import logger

class UsuarioRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UsuarioRepository, cls).__new__(cls)
            cls._instance.__init_singleton(*args, **kwargs)
        return cls._instance

    def __init_singleton(self, *args, **kwargs):
        self.db_connection = DatabaseConnection()
        self.logger = logger
        
    def get_by_name(self, name):
        conn = self.db_connection.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM usuario WHERE nombre = %s"
        cursor.execute(query, (name))
        result = cursor.fetchone()
        cursor.close()
        return Usuario(*result) if result else None