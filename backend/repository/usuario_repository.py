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
        self.db_connection = DatabaseConnection().connect()
        self.logger = logger(self.__class__.__name__)
        
    def get_by_name(self, name):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM usuario WHERE nombre = %s"
        cursor.execute(query, (name))
        result = cursor.fetchone()
        cursor.close()
        return Usuario(*result) if result else None