from sqlalchemy import not_
from backend.models.collection import Coleccion
from backend.models.product import Producto
from backend.shared import db
import os
from flask import jsonify, request, send_from_directory, redirect, url_for, Blueprint, current_app
from backend.controllers.productos_blueprint import retry_on_error

colecciones_blueprint = Blueprint('colecciones', __name__)

#Redirect al update de Colecciones
@colecciones_blueprint.route('/redirectCollection/<int:id>', methods=['GET'])
def get_update_collection_page(id):
    try:
        coleccion = db.session.get(Coleccion, id)

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
        coleccion = Coleccion.query.get(id)
        if not coleccion:
            return jsonify({"error": "Producto no encontrado"}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    
#Metodo Delete para 1 Coleccion
@colecciones_blueprint.route('/deleteCollection/<int:id>', methods=['DELETE'])
def delete_collection(id):
    try:
        coleccion = Coleccion.query.get(id)

        if not coleccion:
            return jsonify({"error": "Producto no encontrado"}), 404 
        
        if coleccion:
            coleccion.esta_eliminada = 1
            Producto.query.filter_by(coleccion_id=id).delete()

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Colección borrada exitosamente"}), 200
    

#Metodo Get para colecciones

@colecciones_blueprint.route('/getAllCollection', methods=['GET'])
@retry_on_error
def get_all_collection():

    colecciones = Coleccion.query.filter(not_(Coleccion.esta_eliminada)).all()
    colecciones_json = [
        {
            'nombre': coleccion.nombre,
            'imgMonocomando': coleccion.img_monocomando,
            'imgBimando': coleccion.img_bimando,
            'imgFreestanding': coleccion.img_freestanding,
            'imgAccesorio': coleccion.img_accesorio,
            'imgComplemento': coleccion.img_complemento,
            'cant_Products': len(coleccion.productos),
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


    
#Metodo Get para 1 Coleccion en particular
@colecciones_blueprint.route('/getCollection/<int:id>', methods=['GET'])
@retry_on_error
def get_coleccion(id):
    try:
        coleccion = Coleccion.query.get(id)
        if not coleccion:
            return jsonify({"error": "Coleccion no encontrado"}), 404
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
                for producto in coleccion.productos
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
        nombre=nombre,
        img_monocomando = imagen_monocomando,
        img_bimando = imagen_bimando,
        img_freestanding = imagen_freestanding,
        img_accesorio = imagen_accesorio,
        img_complemento = imagen_complemento,
        cantidad_productos=0,
        esta_eliminada=False
    )

    db.session.add(nueva_coleccion)
    db.session.commit()

    return redirect(url_for('admin.createCollection'))