from backend.shared import db

class Distribuidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    provincia = db.Column(db.String(255), nullable=False)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    web = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    esta_eliminado = db.Column(db.Boolean, default=False)
    

    def __init__(self, nombre, direccion, provincia, latitud, longitud, web, whatsapp, telefono, esta_eliminado):
        self.nombre = nombre
        self.direccion = direccion
        self.provincia = provincia
        self.latitud = latitud
        self.longitud = longitud
        self.web = web
        self.whatsapp = whatsapp
        self.telefono = telefono
        self.esta_eliminado = esta_eliminado

        
