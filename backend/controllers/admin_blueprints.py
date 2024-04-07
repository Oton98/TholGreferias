from flask import Blueprint, render_template
from backend.controllers.usuario_blueprints import token_requerido

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/interfaceProducts')
@token_requerido
def interfaceProducts():
    return render_template('admin/interfaceProducts.html')

@admin_blueprint.route('/collection')
@token_requerido
def collection():
    return render_template('admin/collection.html')

@admin_blueprint.route('/collections/createCollection')
@token_requerido
def createCollection():
    return render_template('admin/createCollection.html')

@admin_blueprint.route('/faucets')
@token_requerido
def faucets():
    return render_template('admin/faucets.html')

@admin_blueprint.route('/accesories')
@token_requerido
def accesories():
    return render_template('admin/accesories.html')

@admin_blueprint.route('/addons')
@token_requerido
def addons():
    return render_template('admin/addons.html')

@admin_blueprint.route('/createProduct')
@token_requerido
def createProduct():
    return render_template('admin/createProduct.html')

@admin_blueprint.route('/productos/redirectProduct/<int:id>')
@token_requerido
def updateProduct(id):
    return render_template('admin/updateProduct.html') 

@admin_blueprint.route('/admin/distributors')
@token_requerido
def distributors():
    return render_template('admin/distributors.html') 

@admin_blueprint.route('/admin/createDistributor')
@token_requerido
def createDistributor():
    return render_template('admin/createDistributor.html') 