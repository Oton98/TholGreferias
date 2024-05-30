from flask import Flask, jsonify
from flask_cors import CORS
from backend.shared import db
from backend.controllers.distribuidores_blueprint import distribuidores_blueprint
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint
from backend.controllers.admin_blueprints import admin_blueprint
from backend.controllers.usuario_blueprints import usuarios_blueprint, secret_key

from functools import lru_cache
import time
from backend.models.collection import Coleccion
from backend.models.product import Producto

app = Flask(__name__, static_folder='../../static', template_folder='../../templates')
CORS(app)
app.secret_key = secret_key

app.register_blueprint(usuarios_blueprint, url_prefix="/admin")
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/interfaceProducts')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')
app.register_blueprint(distribuidores_blueprint, url_prefix='/distribuidores')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 200
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600

db.init_app(app)

CACHE_EXPIRATION = 8 * 60 * 60
last_cache_update = 0

colecciones_cache = []
productos_cache = []

@lru_cache(maxsize=1)
def cargar_datos_en_cache():
    global last_cache_update
    global colecciones_cache
    global productos_cache
    
    current_time = time.time()

    # Verificar si el caché ha expirado
    if current_time - last_cache_update > CACHE_EXPIRATION:
        last_cache_update = current_time
        # Limpiar el caché actual
        cargar_datos_en_cache.cache_clear()
        # Obtener nuevos datos y guardar en el caché
        colecciones = Coleccion.query.filter(Coleccion.esta_eliminada == False).all()
        productos = Producto.query.filter(Producto.estaDisponible == True).all()
        colecciones_cache = colecciones
        productos_cache = productos
        return colecciones, productos
    else:
        return colecciones_cache, productos_cache

# Esto se ejecutará al cargar el módulo
colecciones_cache, productos_cache = cargar_datos_en_cache()

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()