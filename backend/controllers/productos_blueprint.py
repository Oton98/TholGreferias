from backend.models.collection import Coleccion
from backend.models.product import Producto
from backend.shared import db
import os
from flask import jsonify, request, redirect, url_for, Blueprint

productos_blueprint = Blueprint('productos', __name__)

#Metodo Post para Productos    
@productos_blueprint.route('/createProduct', methods=['POST'])
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

    # Comparo el tipo con su valor en ingles y se lo paso como ruta para que me retorne a la tabla

    ruta_actions = {
        "grifería monocomando": "admin.faucets",
        "grifería bimando": "admin.faucets",
        "grifería freestanding": "admin.faucets",
        "accesorio": "admin.accesories",
        "complemento": "admin.addons"
    }

    coleccion_obj = Coleccion.query.filter_by(nombre=coleccion, esta_eliminada=False).first()

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

        ruta = ruta_actions.get(tipo.lower(), 'default')
        
        return redirect(url_for(ruta))
    
#Metodo Get para 1 Producto en particular
@productos_blueprint.route('/getProduct/<int:id>', methods=['GET'])
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

#Metodo delete para 1 Producto
@productos_blueprint.route('/deleteProduct/<int:id>', methods=['DELETE'])
def delete_producto(id):
    try:
        producto = Producto.query.get(id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        # Obtén la colección asociada al producto
        coleccion = producto.coleccion

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
    
#Redirect al update de Productos
@productos_blueprint.route('/redirectProduct/<int:id>', methods=['GET']) #NO ANDA!
def get_update_product_page(id):
    try:
        producto = db.session.get(Producto, id)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        
        # Construye la URL para el endpoint 'updateProduct' y redirige
        return redirect(url_for('updateProduct'))

    except Exception as e:
        return jsonify({"error": f"Error en la aplicación: {str(e)}"}), 500

#Metodo Put para 1 Producto
@productos_blueprint.route('/updateProduct/<int:id>', methods=['PUT'])
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
            nueva_coleccion = Coleccion.query.filter_by(nombre=nombre_nueva_coleccion, esta_eliminada=False).first()

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
    

#Metodo Get para Accesorios
@productos_blueprint.route('/getAllAccesories', methods=['GET'])    
def get_all_accesories():
    productos = Producto.query.filter_by(tipo='Accesorio').all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Complementos
@productos_blueprint.route('/getAlladdons', methods=['GET'])    
def get_all_addons():
    productos = Producto.query.filter_by(tipo='Complemento').all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Griferias
@productos_blueprint.route('/getAllfaucets', methods=['GET'])    
def get_all_faucets():
    productos = Producto.query.filter(Producto.tipo.like('Grifería%')).all()

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

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
