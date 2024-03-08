from flask import Flask, render_template
from flask_cors import CORS
from backend.shared import db
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint
from backend.controllers.admin_blueprints import admin_blueprint
from backend.controllers.usuario_blueprints import usuarios_blueprint

app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
CORS(app)

app.register_blueprint(usuarios_blueprint, url_prefix= "/admin")
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(admin_blueprint, url_prefix='/interfaceProducts')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()






