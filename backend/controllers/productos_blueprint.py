from backend.models.product import Producto
from flask import jsonify, request, redirect, url_for, Blueprint
from backend.repository.producto_repository import ProductoRepository
from backend.repository.coleccion_repository import ColeccionRepository


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

    cantidadProductoDestacado = ProductoRepository().count_destacados()

    if cantidadProductoDestacado >= 3 and es_destacado:
        return ('error: cantidad maxima de productos destacados superada')
    else:
    
        # Comparo el tipo con su valor en ingles y se lo paso como ruta para que me retorne a la tabla

        ruta_actions = {
            "grifería monocomando": "admin.faucets",
            "grifería bimando": "admin.faucets",
            "grifería freestanding": "admin.faucets",
            "accesorio": "admin.accesories",
            "complemento": "admin.addons"
        }

        coleccion_obj = ColeccionRepository().get_by_name(coleccion)


        if coleccion_obj is None:
            return "La colección especificada no existe", 404
        else:
            nuevo_producto = Producto(
                id = None,
                nombre=nombre,
                tipo=tipo,
                codigo=codigo,
                descripcion=descripcion,
                imagen=imgProducto,
                colores=imgColores,
                manual=linkManualInstalacion,
                medidas=linkManualDetalles,
                esta_disponible=esta_disponible,
                es_destacado=es_destacado,
                coleccion_id=coleccion_obj.id,
            )

            ProductoRepository().create(nuevo_producto)

            ruta = ruta_actions.get(tipo.lower(), 'default')
            
            return redirect(url_for(ruta))
    
#Metodo Get para 1 Producto en particular
@productos_blueprint.route('/getProduct/<int:id>', methods=['GET'])
def get_producto(id):
    try:
        producto = ProductoRepository().get_by_id(id)

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
        producto = ProductoRepository().get_by_id(id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
    
        # Elimina el producto
        ProductoRepository().delete(id)

        return jsonify({"message": "Producto eliminado exitosamente"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
#Metodo Put para 1 Producto
@productos_blueprint.route('/updateProduct/<int:id>', methods=['PUT'])
def update_producto(id):
    try:
        producto = ProductoRepository().get_by_id(id)

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
            nueva_coleccion = ColeccionRepository().get_by_name(nombre_nueva_coleccion)

            if not nueva_coleccion:
                return jsonify({"error": "Colección no encontrada"}), 404

            # Asignar la nueva colección al producto
            producto.coleccion_id = nueva_coleccion.id

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

        ProductoRepository().update(producto)

        return "producto subido exitosamente"

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

#Metodo Get para Accesorios
@productos_blueprint.route('/getAllAccesories', methods=['GET'])   
def get_all_accesories():
    productos = ProductoRepository().get_by_type('Accesorio')

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Complementos
@productos_blueprint.route('/getAlladdons', methods=['GET'])   
def get_all_addons():
    productos = ProductoRepository().get_by_type('Complemento')

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Griferias
@productos_blueprint.route('/getAllfaucets', methods=['GET'])    
def get_all_faucets():
    productos = ProductoRepository().get_by_type_like('Grifería%')

    productos_json = [crear_json_producto(producto) for producto in productos]

    return jsonify(productos_json)

#Metodo Get para Productos Destacados
@productos_blueprint.route('/getallfeatureproducts', methods=['GET'])   
def get_all_featured_products():
    productos = ProductoRepository().get_destacados()

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

#Metodo Get para Productos de una Coleccion
@productos_blueprint.route('/getproductsbycollection/<id>', methods=['GET'])    
def getProductsByCollection(id):
    try:
        productos = ProductoRepository().get_by_coleccion(id)
        productos_json = [{"id": producto.id, "tipo": producto.tipo, "nombre": producto.nombre, "imagen": producto.imagen, "coleccion": producto.coleccion_id} for producto in productos]

        return jsonify({"productos": productos_json})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Método Get para Productos de una Colección por tipo
@productos_blueprint.route('/getproductsbytypebycollection/<int:id>/<tipo>', methods=['GET'])
def get_products_by_type_collection(id, tipo):
    try:
        productos = ProductoRepository().get_by_coleccion_and_type_and_allowed(coleccion_id=id, tipo=tipo)
        # Crear lista de diccionarios para la respuesta JSON
        productos_json = [{"id": producto.id, "nombre": producto.nombre, "imagen": producto.imagen} for producto in productos]

        return jsonify({"productos": productos_json})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def producto_a_diccionario(producto):
    return {
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
