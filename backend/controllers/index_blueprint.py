from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from operator import itemgetter
import smtplib
import time
from flask import Blueprint, jsonify, render_template, request
from backend.controllers.productos_blueprint import producto_a_diccionario
from fuzzywuzzy import process
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
    return render_template('puntosDeVenta.html')

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

    # Diccionario que mapea tipos de colección a columnas de imagen
    columnas_imagenes = {
        "Grifería Bimando": Coleccion.img_bimando,
        "Grifería Monocomando": Coleccion.img_monocomando,
        "Grifería Freestanding": Coleccion.img_freestanding,
        "Accesorio": Coleccion.img_accesorio,
        "Complemento": Coleccion.img_complemento,
    }

    # Obtener la columna de imagen correspondiente al tipo de colección
    columna_imagen = columnas_imagenes[nombre_con_prefijo]

    # Consulta para obtener las colecciones y sus imágenes
    colecciones = (
        Coleccion.query
        .filter(Producto.tipo == nombre_con_prefijo, Coleccion.esta_eliminada == False)
        .join(Producto)
        .add_columns(columna_imagen.label("imagen"))  # Alias para la columna de imagen
        .distinct()
        .all()
    )

    # Preparar datos para la plantilla
    colecciones_data = [{"id": coleccion.id, "nombre": coleccion.nombre, "imgRepresentativa": getattr(coleccion, columna_imagen.key)} for coleccion, imagen in colecciones]
    return render_template('collection.html', colecciones_data=colecciones_data, tipo=nombre_con_prefijo)

@index_blueprint.route('/nuestrodisenio/coleccion-buscada/<string:coleccion>')
def coleccionBuscada(coleccion):
    return render_template('collectionSearch.html', coleccion=coleccion)

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
        remitente_password = 'qmat ghfn ezkj '
        destinatario_correo = 'ventas@thol.com.ar'
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

    for producto_id, producto_nombre, producto_tipo, coleccion_id in productos:
        resultados_combinados.append({
            'tipo': 'Producto',
            'producto_id': producto_id,
            'nombre': producto_nombre,
            'tipo_producto': producto_tipo,
            'coleccion': coleccion_id
        })

    for coleccion in colecciones:
        resultados_combinados.append({
            'tipo': 'Colección',
            'nombre': coleccion.nombre,
        })

    return resultados_combinados

@index_blueprint.route('/searchword/<string:word>', methods=['GET'])
def search_word(word):
    colecciones = Coleccion.query.filter(Coleccion.esta_eliminada == False).all()

    # Realizar la consulta para obtener productos disponibles
    productos = Producto.query.filter(Producto.estaDisponible == True).all()

    # Obtener solo el nombre de productos y cambiar coleccion_id por nombre de colección
    nombres_productos = [
        (
            producto.id, 
            producto.nombre, 
            producto.tipo, 
            next((coleccion.nombre for coleccion in colecciones if coleccion.id == producto.coleccion_id), None)
        )
        for producto in productos
    ]

    # Obtener solo los nombres y tipos de productos para la búsqueda con process.extract
    nombres_tipos_productos_para_busqueda = [(producto[1], producto[2]) for producto in nombres_productos]

    # Encuentra las coincidencias más cercanas basadas solo en el nombre y tipo de productos
    coincidencias = process.extract(word, nombres_tipos_productos_para_busqueda, limit=5)

    print(coincidencias)

    coincidencias_nombres_tipos = [coincidencia[0] for coincidencia in coincidencias if coincidencia[1] > 50]
    
    # Filtrar los productos que coinciden con los nombres y tipos
    productos_coincidentes = [
        producto for producto in nombres_productos 
        if (producto[1], producto[2]) in coincidencias_nombres_tipos
    ]

    colecciones_coincidencias = Coleccion.query.filter(Coleccion.esta_eliminada == False, Coleccion.nombre.like(f'{word}%')).all()

    resultados_combinados = combinar_resultados(productos_coincidentes, colecciones_coincidencias)

    return jsonify(resultados_combinados)