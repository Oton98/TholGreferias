from flask import Flask
from flask_cors import CORS
from backend.shared import db
from datetime import timedelta

from backend.controllers.distribuidores_blueprint import distribuidores_blueprint
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint
from backend.controllers.admin_blueprints import admin_blueprint
from backend.controllers.usuario_blueprints import usuarios_blueprint, secret_key

app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
# app = Flask(__name__, static_folder = 'static', template_folder='templates')
CORS(app)
app.secret_key = secret_key

app.register_blueprint(usuarios_blueprint, url_prefix= "/admin")
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/interfaceProducts')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')
app.register_blueprint(distribuidores_blueprint, url_prefix='/distribuidores')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://thol_thol:Thol/97531@localhost/thol_thol'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 200 
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600

# app.config['SESSION_COOKIE_NAME'] = 'session_id'
# app.config['SESSION_COOKIE_SECURE'] = False
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
# app.config['SESSION_COOKIE_DOMAIN'] = "www.thol.com.ar"

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()






