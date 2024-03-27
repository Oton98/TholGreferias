from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from flask import Blueprint, jsonify, render_template, request
from backend.controllers.productos_blueprint import producto_a_diccionario
from backend.models.collection import Coleccion

from backend.models.product import Producto


index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')

@index_blueprint.route('/index')
def index():
    return render_template('index.html')

@index_blueprint.route('/admin-login')
def interno():
    return render_template('admin/login.html')

@index_blueprint.route('/nuestrodisenio')
def nuestroDisenio():
    return render_template('nuestroDisenio.html')

@index_blueprint.route('/puntosdeventa')
def puntosDeVenta():
    return render_template('puntosdeventa.html')

@index_blueprint.route('/personalizacion')
def personalizacion():
    return render_template('personalizacion.html')

@index_blueprint.route('/consulta')
def consulta():
    return render_template('consulta.html')

@index_blueprint.route('producto/<producto>')
def productoIndex():
    return render_template('producto.html')

@index_blueprint.route('nuestrodisenio/coleccion/<string:nombre>')
def coleccionIndex(nombre):
    tipoTarjetasNombre = ["Grifería Bimando", "Grifería Monocomando", "Grifería Freestanding", "Accesorio", "Complemento"]
    nombre_con_prefijo = f"Grifería {nombre}" if nombre not in ["Accesorio", "Complemento"] else nombre

    if nombre_con_prefijo not in tipoTarjetasNombre:
        return "Tipo de producto no válido", 404

    colecciones = Coleccion.query.join(Producto).filter(Producto.tipo==nombre_con_prefijo, Coleccion.esta_eliminada==False).distinct().all()
    colecciones_data = [{"id": coleccion.id, "nombre": coleccion.nombre, "imgRepresentativa": coleccion.imgRepresentativa} for coleccion in colecciones]
    return render_template('collection.html', colecciones_data = colecciones_data, tipo=nombre_con_prefijo)


@index_blueprint.route('/nuestrodisenio/coleccion/<string:nombre>/productmenu/<tipo>')
def productoMenuTipo(nombre, tipo):
    coleccion = Coleccion.query.filter_by(nombre=nombre, esta_eliminada=False).first()
    productos = Producto.query.filter_by(coleccion_id=coleccion.id, tipo=tipo).all()
    productos_info = [{"id": producto.id, "nombre": producto.nombre, "imagen": producto.imagen, "tipo": producto.tipo} for producto in productos]
    return render_template('productMenu.html', coleccion=coleccion, productos_info=productos_info)

@index_blueprint.route('/nuestrodisenio/coleccion/<string:nombre>/productmenu/<tipo>/product/<int:id>')
def productSelection(nombre, tipo, id):
    coleccion = Coleccion.query.filter_by(nombre=nombre, esta_eliminada=False).first()
    producto = Producto.query.filter_by(coleccion_id=coleccion.id, tipo=tipo, id=id).first()
    
    if producto is not None:
        # Crear un diccionario que solo contenga el id del producto
        producto_dict = {"id": producto.id}
        return render_template('product.html', coleccion=coleccion, producto=producto_dict)
    else:
        return "Producto no encontrado", 404

@index_blueprint.route('/enviarCorreo', methods=['POST'])
def enviarCorreo():
    try:
        data = request.json

        nombre = data.get('nombre', '')
        asunto = data.get('asunto', '')
        correo = data.get('email', '')
        mensaje = data.get('mensaje', '')

        # Tengo que ver como hacer las credenciales con Thol
        remitente_correo = 'joaquindiago98@gmail.com'
        remitente_password = 'qmat ghfn ezkj rzaf'
        destinatario_correo = 'joaquindiago98@gmail.com'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Configura el mensaje
        msg = MIMEMultipart()
        msg['From'] = remitente_correo
        msg['To'] = destinatario_correo
        msg['Subject'] = f'Mensaje de {nombre} - {asunto}'
        cuerpo_mensaje = f'Nombre: {nombre}\nCorreo: {correo}\n\n{mensaje}'
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

        # Inicia la conexión SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(remitente_correo, remitente_password)
            server.sendmail(remitente_correo, destinatario_correo, msg.as_string())

        return jsonify({'mensaje': 'Correo enviado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def combinar_resultados(productos, colecciones):
    resultados_combinados = []

    for producto in productos:
        resultados_combinados.append({
            'tipo': 'producto',
            'nombre': producto.nombre,
        })

    for coleccion in colecciones:
        resultados_combinados.append({
            'tipo': 'coleccion',
            'nombre': coleccion.nombre,
        })

    return resultados_combinados

@index_blueprint.route('/searchword/<string:word>', methods=['GET'])
def search_word(word):
    productos = Producto.query.filter(Producto.nombre.like(f'{word}%')).all()
    colecciones = Coleccion.query.filter(Coleccion.nombre.like(f'{word}%')).all()

    time.sleep(2)

    resultados_combinados = combinar_resultados(productos, colecciones)

    return jsonify(resultados_combinados)