from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/interfaceProducts')
def interfaceProducts():
    return render_template('admin/interfaceProducts.html')

@admin_blueprint.route('/collections')
def collections():
    return render_template('admin/collections.html')

@admin_blueprint.route('/collections/createCollection')
def createCollection():
    return render_template('admin/createCollection.html')

@admin_blueprint.route('/faucets')
def faucets():
    return render_template('admin/faucets.html')

@admin_blueprint.route('/accesories')
def accesories():
    return render_template('admin/accesories.html')

@admin_blueprint.route('/addons')
def addons():
    return render_template('admin/addons.html')

@admin_blueprint.route('/createProduct')
def createProduct():
    return render_template('admin/createProduct.html')

@admin_blueprint.route('/productos/redirectProduct/<int:id>')
def updateProduct(id):
    return render_template('admin/updateProduct.html') 