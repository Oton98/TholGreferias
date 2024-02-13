from flask import Flask, send_from_directory, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50))
    codigo = db.Column(db.Integer)
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

class Coleccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    cantidad_Productos = db.Column(db.Integer, default=0)
    productos = db.relationship('Producto', back_populates='coleccion')

    def __init__(self, nombre):
        self.nombre = nombre
        
    def obtener_productos(self):
        # Método para obtener todos los productos vinculados a la colección
        return Producto.query.filter_by(coleccion=self).all()

# Función para actualizar la cantidad de productos antes de cada commit
def actualizar_cantidad_productos(mapper, connection, target):
    target.cantidad_Productos = len(target.productos)

# Asociar el evento a la clase Coleccion
event.listen(Coleccion, 'before_insert', actualizar_cantidad_productos)
event.listen(Coleccion, 'before_update', actualizar_cantidad_productos)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

#Metodo Get para Accesorios
@app.route('/getAllAccesories', methods=['GET'])    
def get_all_accesories():
    productos = Producto.query.filter_by(tipo='Accesorio').all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Complementos
@app.route('/getAlladdons', methods=['GET'])    
def get_all_addons():
    productos = Producto.query.filter_by(tipo='Complemento').all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Griferias
@app.route('/getAllfaucets', methods=['GET'])    
def get_all_faucets():
    productos = Producto.query.filter(Producto.tipo.like('Grifería%')).all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para colecciones

@app.route('/getAllCollection', methods=['GET'])
def get_all_collections():

    colecciones = Coleccion.query.all()

    colecciones_json = [
        {
            'nombre': coleccion.nombre,
            'cant_Products': coleccion.cantidad_Productos,
            'productos': [
                {
                    'nombre_producto': producto.nombre,
                }
                for producto in coleccion.productos
            ]
        }
        for coleccion in colecciones
    ]

    return jsonify(colecciones_json)

#Metodo Post para Productos    
@app.route('/createProduct', methods=['POST'])
def add_product():
    
    # Obtener datos del formulario
    nombre = request.form.get('productName')
    tipo = request.form.get('productType')
    codigo = request.form.get('productCode')
    descripcion = request.form.get('descriptionProduct')
    imgProducto = request.form.get('productImage')
    imgColores = request.form.get('productColores')
    linkManualInstalacion = request.form.get('collectionManualInstalation')
    linkManualDetalles = request.form.get('collectionManualDetails')
    es_destacado = request.form.get('isFeaturedProducto') == 'on'
    esta_disponible = request.form.get('isAvailable') == 'on'
    coleccion = request.form.get('collection')

    coleccion_obj = Coleccion.query.filter_by(nombre=coleccion).first()

    if coleccion_obj is None:
        return "La colección especificada no existe", 404
    else:
        nuevo_producto = Producto(
            nombre=nombre,
            tipo=tipo,
            codigo=codigo,
            descripcion=descripcion,
            imagen=imgProducto,
            colores=imgColores,
            manual=linkManualInstalacion,
            medidas=linkManualDetalles,
            esta_disponible=es_destacado,
            es_destacado=esta_disponible,
            coleccion=coleccion_obj 
        )

        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for('static', filename='admin/createProduct.html'))

#Metodo Post1 para colecciones
@app.route('/createCollection', methods=['POST'])
def add_Colecction():
    nombre = request.form.get('CollectionName')

    nueva_coleccion = Coleccion(
        nombre = nombre
    )

    db.session.add(nueva_coleccion)
    db.session.commit()

    return redirect(url_for('static', filename='admin/createCollection.html'))

def crear_json_producto(producto):
    return {
        'id': producto.id,
        'nombre': producto.nombre,
        'tipo': producto.tipo,
        'codigo': producto.codigo,
        'descripcion': producto.descripcion,
        'imagen': producto.imagen,
        'colores': producto.colores,
        'manual': producto.manual,
        'medidas': producto.medidas,
        'estaDisponible': producto.estaDisponible,
        'esDestacado': producto.esDestacado,
        'coleccion': producto.coleccion.nombre if producto.coleccion else None
    }

if __name__ == '__main__':
    app.run(port=5000, debug=True)
