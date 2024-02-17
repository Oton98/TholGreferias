from flask import Flask, send_from_directory, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import not_
from sqlalchemy import event
from flask_cors import CORS
import os

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
    cantidad_productos = db.Column(db.Integer, default=0)
    esta_eliminada = db.Column(db.Boolean, default=False)
    productos = db.relationship('Producto', back_populates='coleccion')

    def __init__(self, nombre, cantidad_productos=0, esta_eliminada=False): 
        self.nombre = nombre
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

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

#Redirect al update
@app.route('/redirectProduct/<int:id>', methods=['GET'])
def get_update_page(id):
    try:
        producto = db.session.get(Producto, id)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        # Obtén la ruta completa del archivo update.html
        file_path = os.path.join(app.root_path, 'static', 'admin')

        # Imprime información de depuración
        print(f'File Path: {file_path}')
        print(f'Requested URL: {request.url}')


        # Envía el archivo desde el directorio
        return send_from_directory(file_path, 'update.html')

    except Exception as e:
        return jsonify({"error": f"Error en la aplicación: {str(e)}"}), 500


#Metodo delete para 1 Producto
@app.route('/deleteProduct/<int:id>', methods=['DELETE'])
def delete_producto(id):
    try:
        producto = Producto.query.get(id)
        print(producto)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        # Obtén la colección asociada al producto
        coleccion = producto.coleccion
        print(coleccion)

        # Decrementa la columna cantidad_Productos en uno
        if coleccion:
            if coleccion.cantidad_productos > 0:
                coleccion.cantidad_productos -= 1

        # Elimina el producto
        db.session.delete(producto)
        db.session.commit()

        return jsonify({"message": "Producto eliminado exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

#Metodo Put para 1 Producto
@app.route('/updateProduct/<int:id>', methods=['PUT'])
def update_producto(id):
    try:
        producto = Producto.query.get(id)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        data = request.json

        nombre = data.get('nombre', producto.nombre)
        tipo = data.get('tipo', producto.tipo)
        codigo = data.get('codigo', producto.codigo)
        descripcion = data.get('descripcion', producto.descripcion)
        imagen = data.get('imagen', producto.imagen)
        colores = data.get('colores', producto.colores)
        manual = data.get('manual', producto.manual)
        medidas = data.get('medidas', producto.medidas)
        estaDisponible = data.get('estaDisponible', producto.estaDisponible)
        esDestacado = data.get('esDestacado', producto.esDestacado)

       # Obtener el nombre de la nueva colección desde los datos recibidos
        nombre_nueva_coleccion = data.get('coleccion')

        if nombre_nueva_coleccion is not None:
            # Buscar la colección por nombre
            nueva_coleccion = Coleccion.query.filter_by(nombre=nombre_nueva_coleccion).first()

            if not nueva_coleccion:
                return jsonify({"error": "Colección no encontrada"}), 404

            # Actualizar la cantidad de productos en la colección actual
            if producto.coleccion:
                producto.coleccion.cantidad_productos -= 1

            # Asignar la nueva colección al producto
            producto.coleccion = nueva_coleccion
            nueva_coleccion.cantidad_productos += 1

        producto.nombre = nombre
        producto.tipo = tipo
        producto.codigo = codigo
        producto.descripcion = descripcion
        producto.imagen = imagen
        producto.colores = colores
        producto.manual = manual
        producto.medidas = medidas
        producto.estaDisponible = estaDisponible
        producto.esDestacado = esDestacado

        db.session.commit()

        return "producto subido exitosamente"

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
#Metodo Put para 1 Coleccion
    
#Metodo Delete para 1 Coleccion
@app.route('/deleteCollection/<int:id>', methods=['DELETE'])
def delete_collection(id):
    try:
        coleccion = Coleccion.query.get(id)

        if not coleccion:
            return jsonify({"error": "Producto no encontrado"}), 404 
        
        if coleccion:
            coleccion.esta_eliminada = 1

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Colección borrada exitosamente"}), 200
    
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

    colecciones = Coleccion.query.filter(not_(Coleccion.esta_eliminada)).all()
    print(colecciones)
    colecciones_json = [
        {
            'nombre': coleccion.nombre,
            'cant_Products': coleccion.cantidad_productos,
            'id': coleccion.id,
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

#Metodo Get para 1 Producto en particular
@app.route('/getProduct/<int:id>', methods=['GET'])
def get_producto(id):
    try:
        producto = Producto.query.get(id)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        producto_data = {
            "id": producto.id,
            "nombre": producto.nombre,
            "tipo": producto.tipo,
            "codigo": producto.codigo,
            "descripcion": producto.descripcion,
            "imagen": producto.imagen,
            "colores": producto.colores,
            "manual": producto.manual,
            "medidas": producto.medidas,
            "estaDisponible": producto.estaDisponible,
            "esDestacado": producto.esDestacado,
            "coleccion_id": producto.coleccion_id
        }

        return jsonify(producto_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Metodo Get para 1 Coleccion en particular
@app.route('/getCollection/<int:id>', methods=['GET'])
def get_coleccion(id):
    try:
        coleccion = Coleccion.query.get(id)
        if not coleccion:
            return jsonify({"error": "Coleccion no encontrado"}), 404
        coleccion_data ={
            'id': coleccion.id,
            'nombre': coleccion.nombre,
            'cantidad_productos': coleccion.cantidad_productos,
            'productos': [
                {   
                    'id': producto.id,
                    'nombre_producto': producto.nombre,
                }
                for producto in coleccion.productos
            ]

        }

        return jsonify(coleccion_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


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
def add_Coleccion():
    nombre = request.form.get('CollectionName')

    nueva_coleccion = Coleccion(
        nombre=nombre,
        cantidad_productos=0,
        esta_eliminada=False
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
