from backend.models.usuario import Usuario
from flask import jsonify, request, Blueprint
from werkzeug.security import check_password_hash


usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route('/login', methods=['POST'])
def login():
    nombre = request.json.get('userName')
    pwd = request.json.get('userPassword')

    if nombre == 'BurgemeisterThol2024':
        usuario = Usuario.query.filter_by(nombre=nombre).first()

        if usuario and check_password_hash(usuario.password, pwd):
            return jsonify({'redirect': '/interfaceProducts/interfaceProducts'})
        else:
            return jsonify({'redirect': '/admin/login'})

    return jsonify({'success': False})