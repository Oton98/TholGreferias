from backend.models.usuario import Usuario
from flask import jsonify, render_template, request, Blueprint, session
from itsdangerous import URLSafeTimedSerializer as Serializer
from functools import wraps
from repository.usuario_repository import UsuarioRepository
import bcrypt

usuarios_blueprint = Blueprint('usuarios', __name__)

secret_key = "264e7d7c0b594b5351081af6d2c83367"
s = Serializer(secret_key)

@usuarios_blueprint.route('/login', methods=['POST'])
def login():
    nombre = request.json.get('userName')
    pwd = request.json.get('userPassword')

    if nombre == 'BurgemeisterThol2024':
        usuario = UsuarioRepository().get_by_name(nombre)

        if usuario and bcrypt.checkpw(pwd.encode("utf-8"), usuario.password.encode("utf-8")):
            token = s.dumps({})
            session["token"] = token
            return jsonify({'redirect': '/interfaceProducts/interfaceProducts'})

        else:
            return jsonify({'redirect': '/admin/login'})

    else:
        return jsonify({'redirect': '/admin/login'})

def token_requerido(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        token = session.get('token')
        try:
          data = s.loads(token, max_age=3600)
          return f(*args, **kwargs)
        except Exception as e:
          return render_template('admin/login.html')  
    return decorada