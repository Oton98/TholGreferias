from flask import Flask, render_template
from flask_cors import CORS
from backend.shared import db
from backend.controllers.colecciones_blueprint import colecciones_blueprint
from backend.controllers.productos_blueprint import productos_blueprint
from backend.controllers.index_blueprint import index_blueprint

app = Flask(__name__, static_folder = '../../static', template_folder='../../templates')
CORS(app)

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
    return render_template('admin/createCollection.html')

@app.route('/interfaceProducts/faucets')
def faucets():
    return render_template('admin/faucets.html')

@app.route('/interfaceProducts/accesories')
def accesories():
    return render_template('admin/accesories.html')

@app.route('/interfaceProducts/addons')
def addons():
    return render_template('admin/addons.html')

@app.route('/interfaceProducts/createProduct')
def createProduct():
    return render_template('admin/createProduct.html')

@app.route('/interfaceProducts/productos/redirectProduct/<int:id>')
def updateProduct(id):
    return render_template('admin/updateProduct.html') 

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(colecciones_blueprint, url_prefix='/colecciones')
app.register_blueprint(productos_blueprint, url_prefix='/productos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:firewall15@localhost/thol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()






