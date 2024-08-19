from backend.models.collection import Coleccion
from backend.repository.coleccion_repository import ColeccionRepository
from backend.repository.producto_repository import ProductoRepository
import os
from flask import jsonify, request, send_from_directory, redirect, url_for, Blueprint, current_app

colecciones_blueprint = Blueprint('colecciones', __name__)

#Redirect al update de Colecciones
@colecciones_blueprint.route('/redirectCollection/<int:id>', methods=['GET'])
def get_update_collection_page(id):
    try:
        coleccion = ColeccionRepository().get_by_id(id)

        if not coleccion:
            return jsonify({"error": "Coleccion no encontrado"}), 404

        # Obtén la ruta completa del archivo update.html
        file_path = os.path.join(current_app.blueprints['colecciones'].root_path, 'static', 'admin')
        # Envía el archivo desde el directorio
        return send_from_directory(file_path, 'updateCollection.html')

    except Exception as e:
        return jsonify({"error": f"Error en la aplicación: {str(e)}"}), 500
    

    
#Metodo Put para 1 Coleccion
@colecciones_blueprint.route('/updateCollection/<int:id>', methods=['PUT'])
def update_collection(id):
    try:
        coleccion = ColeccionRepository().get_by_id(id)
        if not coleccion:
            return jsonify({"error": "Producto no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
#Metodo Delete para 1 Coleccion
@colecciones_blueprint.route('/deleteCollection/<int:id>', methods=['DELETE'])
def delete_collection(id):
    try:
        coleccion = ColeccionRepository().get_by_id(id)

        if not coleccion:
            return jsonify({"error": "Producto no encontrado"}), 404 
        
        if coleccion:
            coleccion.esta_eliminada = 1
            ColeccionRepository().update(coleccion=coleccion, coleccion_id=coleccion.id)
            ProductoRepository().delete_by_coleccion_id(coleccion_id=id)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Colección borrada exitosamente"}), 200
    

#Metodo Get para colecciones

@colecciones_blueprint.route('/getAllCollection', methods=['GET'])
def get_all_collection():

    colecciones = ColeccionRepository().get_all()
    
    colecciones_json = [
        {
            'nombre': coleccion.nombre,
            'imgMonocomando': coleccion.img_monocomando,
            'imgBimando': coleccion.img_bimando,
            'imgFreestanding': coleccion.img_freestanding,
            'imgAccesorio': coleccion.img_accesorio,
            'imgComplemento': coleccion.img_complemento,
            'id': coleccion.id
        }
        for coleccion in colecciones
    ]

    return jsonify(colecciones_json)


    
#Metodo Get para 1 Coleccion en particular
@colecciones_blueprint.route('/getCollection/<int:id>', methods=['GET'])
def get_coleccion(id):
    try:
        coleccion = ColeccionRepository().get_by_id(id)
        if not coleccion:
            return jsonify({"error": "Coleccion no encontrado"}), 404
        
        productos = ProductoRepository().get_by_coleccion(id)
        coleccion_data ={
            'id': coleccion.id,
            'imgMonocomando': coleccion.img_monocomando,
            'imgBimando': coleccion.img_bimando,
            'imgFreestanding': coleccion.img_freestanding,
            'imgAccesorio': coleccion.img_accesorio,
            'imgComplemento': coleccion.img_complemento,
            'nombre': coleccion.nombre,
            'cantidad_productos': coleccion.cantidad_productos,
            'productos': [
                {   
                    'id': producto.id,
                    'nombre_producto': producto.nombre,
                }
                for producto in productos
            ]

        }

        return jsonify(coleccion_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Metodo Post1 para colecciones
@colecciones_blueprint.route('/createCollection', methods=['POST'])
def add_Coleccion():
    nombre = request.form.get('CollectionName')
    imagen_bimando = request.form.get('CollectionImgBimandos')
    imagen_monocomando = request.form.get('CollectionImgMonocomandos')
    imagen_freestanding = request.form.get('CollectionImgFreestandings')
    imagen_complemento = request.form.get('CollectionImgComplementos')
    imagen_accesorio = request.form.get('CollectionImgAccesorios')

    nueva_coleccion = Coleccion(
        id=None,
        nombre=nombre,
        img_monocomando = imagen_monocomando,
        img_bimando = imagen_bimando,
        img_freestanding = imagen_freestanding,
        img_accesorio = imagen_accesorio,
        img_complemento = imagen_complemento,
        cantidad_productos=0,
        esta_eliminada=False
    )

    ColeccionRepository().create(nueva_coleccion)

    return redirect(url_for('admin.createCollection'))