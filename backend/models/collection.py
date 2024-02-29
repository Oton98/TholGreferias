from sqlalchemy import event
from backend.models.product import Producto
from backend.shared import db

class Coleccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    imgRepresentativa = db.Column(db.String(255), nullable=False)
    cantidad_productos = db.Column(db.Integer, default=0)
    esta_eliminada = db.Column(db.Boolean, default=False)
    productos = db.relationship('Producto', back_populates='coleccion')

    def __init__(self, nombre, imgRepresentativa, cantidad_productos=0, esta_eliminada=False): 
        self.nombre = nombre
        self.imgRepresentativa = imgRepresentativa
        self.cantidad_productos = cantidad_productos
        self.esta_eliminada = esta_eliminada

    def obtener_productos(self):
        # Método para obtener todos los productos vinculados a la colección
        return Producto.query.filter_by(coleccion=self).all()
    
# Función para actualizar la cantidad de productos antes de cada commit
def actualizar_cantidad_productos(mapper, connection, target):
    target.cantidad_productos = len(target.productos)

# Asociar el evento a la clase Coleccion
event.listen(Coleccion, 'before_insert', actualizar_cantidad_productos)
event.listen(Coleccion, 'before_update', actualizar_cantidad_productos)