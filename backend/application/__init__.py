from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from backend.shared import db
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint

app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
CORS(app)



@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/nuestroDiseño')
def nuestroDisenio():
    return render_template('nuestroDisenio.html')

@app.route('/puntosDeVenta')
def puntosDeVenta():
    return render_template('puntosDeVenta.html')

@app.route('/personalizacion')
def personalizacion():
    return render_template('personalizacion.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/admin-login')
def interno():
    return render_template('admin/login.html')

@app.route('/interfaceProducts')
def interfaceProducts():
    return render_template('admin/interfaceProducts.html')

@app.route('/interfaceProducts/collections')
def collections():
    return render_template('admin/collections.html')

@app.route('/interfaceProducts/collections/createCollection')
def createCollection():
    return render_template('admin/createCollection.html', id)

app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()






