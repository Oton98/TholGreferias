from backend.models.usuario import Usuario
from backend.shared import db
import os
from flask import jsonify, request, redirect, url_for, Blueprint

usuarios_blueprint = Blueprint('usuarios', __name__)

# @usuarios_blueprint.route('/login', methods=['POST'])
# def inicio_sesion():
#     nombre = request.form.get('userName')
#     pwd = request.form.get('userPassword')