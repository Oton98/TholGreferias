from flask import jsonify, render_template, request, Blueprint
from backend.models.distribuidores import Distribuidor
from backend.shared import db
from sqlalchemy import not_

distribuidores_blueprint = Blueprint('distribuidores', __name__)

@distribuidores_blueprint.route("/createdistributor", methods=['POST'])
def add_Distribuidor():
    nombre = request.form.get('DistributorName')
    direccion = request.form.get('DistributorAdress')
    provincia = request.form.get('ProvinciaAdress')
    latitud = float(request.form.get('DistributorLatitude'))
    longitud = float(request.form.get('DistributorLength'))

    nuevo_distribuidor = Distribuidor(
        nombre = nombre,
        direccion = direccion,
        provincia = provincia,
        latitud = latitud,
        longitud = longitud,
        esta_eliminado = False
    )

    db.session.add(nuevo_distribuidor)
    db.session.commit()

    return render_template('admin/distributors.html')


# @distribuidores_blueprint.route("/updatedistributor/<int:id>")

@distribuidores_blueprint.route("/delatedistributor/<int:id>", methods=['DELETE'])
def delete_distributor(id):
    try:
        distribuidor = Distribuidor.query.get(id)

        if not distribuidor:
            return jsonify({"error": "Producto no encontrado"}), 404
        
        if distribuidor:
            distribuidor.esta_eliminado = 1

        db.session.commit()

    except Distribuidor as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Colección borrada exitosamente"}), 200

# @distribuidores_blueprint.route("/getdistributor/<int:id>")

@distribuidores_blueprint.route("/getalldistributors", methods=['GET'])
def get_all_distributors():

    distribuidores = Distribuidor.query.filter(not_(Distribuidor.esta_eliminado)).all()
    distribuidores_json = [
        {   
            'id': distrbuidor.id,
            'nombre': distrbuidor.nombre,
            'direccion': distrbuidor.direccion,
            'provincia': distrbuidor.provincia,
            'latitud': distrbuidor.latitud,
            'longitud': distrbuidor.longitud,

        }
        for distrbuidor in distribuidores
    ]
    return jsonify(distribuidores_json)