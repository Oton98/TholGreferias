from flask import Flask
from flask_cors import CORS
from backend.shared import db 
from backend.controllers.distribuidores_blueprint import distribuidores_blueprint
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint
from backend.controllers.admin_blueprints import admin_blueprint
from backend.controllers.usuario_blueprints import usuarios_blueprint, secret_key

# app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
app = Flask(__name__, static_folder = 'static', template_folder='templates')

CORS(app)
app.secret_key = secret_key

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://thol_thol:Thol/97531@localhost/thol_thol'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 1800,
    'pool_timeout': 30,
    'pool_size': 20,
    'max_overflow': 0,
}

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Registrar blueprints con la caché como argumento
app.register_blueprint(usuarios_blueprint, url_prefix="/admin")
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/interfaceProducts')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')
app.register_blueprint(distribuidores_blueprint, url_prefix='/distribuidores')

if __name__ == '__main__':
    app.run(debug=True)
