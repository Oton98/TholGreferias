from werkzeug.security import check_password_hash

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
    
    @classmethod
    def check_password(self, password_hasheada, password):
        return check_password_hash(password_hasheada, password)
    
        
