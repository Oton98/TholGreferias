from backend.shared import db
from werkzeug.security import check_password_hash, generate_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
    
    @classmethod
    def check_password(self, password_hasheada, password):
        return check_password_hash(password_hasheada, password)
    
# print(generate_password_hash("Griferias#49257106Thol"))
        
