from backend.shared import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50))
    codigo = db.Column(db.String(255))
    descripcion = db.Column(db.String(1000))
    imagen = db.Column(db.String(255))
    colores = db.Column(db.String(255))
    manual = db.Column(db.String(255))
    medidas = db.Column(db.String(255))
    estaDisponible = db.Column(db.Boolean) 
    esDestacado = db.Column(db.Boolean)
    coleccion_id = db.Column(db.Integer, db.ForeignKey('coleccion.id'))
    coleccion = db.relationship('Coleccion', back_populates='productos')

    def __init__(self, nombre, tipo, codigo, descripcion, imagen, colores, manual, medidas, esta_disponible, es_destacado, coleccion):
        self.nombre = nombre
        self.tipo = tipo
        self.codigo = codigo
        self.descripcion = descripcion
        self.imagen = imagen
        self.colores = colores
        self.manual = manual
        self.medidas = medidas
        self.estaDisponible = esta_disponible
        self.esDestacado = es_destacado
        self.coleccion = coleccion