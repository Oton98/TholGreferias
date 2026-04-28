from flask import Flask
from flask_cors import CORS
from backend.controllers.distribuidores_blueprint import distribuidores_blueprint
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint
from backend.controllers.admin_blueprints import admin_blueprint
from backend.controllers.usuario_blueprints import usuarios_blueprint, secret_key
# from backend.controllers.special_blueprint

app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
# app = Flask(__name__, static_folder = 'static', template_folder='templates')

CORS(app)
app.secret_key = secret_key

# Registrar blueprints con la caché como argumento
app.register_blueprint(usuarios_blueprint, url_prefix="/admin")
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/interfaceProducts')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')
app.register_blueprint(distribuidores_blueprint, url_prefix='/distribuidores')
# app.register_blueprint(special_blueprint, url_prefix='/special')

if __name__ == '__main__':
    app.run(debug=True)
