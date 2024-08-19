from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from backend.shared import logger
import smtplib
import json
from flask import Blueprint, jsonify, render_template, request
from fuzzywuzzy import process
from backend.controllers.cache import Cache
from repository.coleccion_repository import ColeccionRepository
from repository.distribuidor_repository import DistribuidorRepository
from repository.producto_repository import ProductoRepository


index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')

@index_blueprint.route('/index')
def index():
    return render_template('index.html')

@index_blueprint.route('/admin-login')
def interno():
    return render_template('admin/login.html')

@index_blueprint.route('/prueba')
def prueba():
    return render_template('prueba.html')

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

def obtener_colecciones():
    cache = Cache()
    colecciones = cache.get("colecciones")
    if colecciones is None:
        colecciones = ColeccionRepository().get_all()
        cache.put("colecciones", colecciones, 28800)
        logger.info("colecciones obtenidas de la base de datos")
    else:
        logger.info("colecciones obtenidas de la caché")
    return colecciones
 
def obtener_productos():
    cache = Cache()
    productos = cache.get("productos")
    if productos is None:
        productos = ProductoRepository().get_all()
        cache.put("productos", productos, 28800)
        logger.info("productos obtenidos de la base de datos")
    else:
        logger.info("productos obtenidos de la caché")
    return productos

def obtener_distribuidores():
    cache = Cache()
    distribuidores = cache.get("distribuidores")
    if distribuidores is None: 
        distribuidores = DistribuidorRepository.get_all()
        cache.put("distribuidores", distribuidores, 28800)
        logger.info("distribuidores obtenidos de la base de datos")
    else:
        logger.info("distribuidores obtenidos de la caché")
    return distribuidores

def obtener_coleccion_por_nombre(nombre):
    cache = Cache()
    cache_key = "coleccion_" + nombre
    coleccion = cache.get(cache_key)
    if coleccion is None:
        coleccion = ColeccionRepository().get_by_name(nombre)
        if coleccion is not None:
            cache.put(cache_key, coleccion, 28800)
            logger.info("colección obtenida de la base de datos")
    else:
        logger.info("colección obtenida de la caché")
    return coleccion

def obtener_producto_por_coleccion_y_tipo(coleccion_id, tipo):
    cache = Cache()
    cache_key = f"productos_{coleccion_id}_{tipo}"
    productos_info = cache.get(cache_key)

    if productos_info is None:
        productos = ProductoRepository().get_by_coleccion_and_type(coleccion_id, tipo)
        productos_info = [{"id": producto.id, "nombre": producto.nombre, "imagen": producto.imagen, "tipo": producto.tipo} for producto in productos]
        cache.put(cache_key, productos_info, 28800)
        logger.info("productos obtenidos de la base de datos")
    else:
        logger.info("productos obtenidos de la caché")
    return productos_info

def obtener_producto_coleccion_tipo_id(coleccion_id, tipo, id):
    cache = Cache()
    cache_key = f"producto_{coleccion_id}_{tipo}_{id}"
    producto = cache.get(cache_key)

    if producto is None:
        producto_obj = ProductoRepository().get_by_coleccion_type_and_id(coleccion_id=coleccion_id, tipo=tipo, producto_id=id)
        if producto_obj is not None:
            producto = {"id": producto_obj.id, "nombre": producto_obj.nombre, "imagen": producto_obj.imagen, "tipo": producto_obj.tipo}
            cache.put(cache_key, producto, 28800)
            logger.info("producto obtenido de la base de datos")
    else:
        logger.info("producto obtenido de la caché")
    return producto

@index_blueprint.route('nuestrodisenio/coleccion/<string:nombre>')
def coleccionIndex(nombre):
    tipoTarjetasNombre = ["Grifería Bimando", "Grifería Monocomando", "Grifería Freestanding", "Accesorio", "Complemento"]
    nombre_con_prefijo = f"Grifería {nombre}" if nombre not in ["Accesorio", "Complemento"] else nombre

    if nombre_con_prefijo not in tipoTarjetasNombre:
        return "Tipo de producto no válido", 404

    columnas_imagenes = {
        "Grifería Bimando": "img_bimando",
        "Grifería Monocomando": "img_monocomando",
        "Grifería Freestanding": "img_freestanding",
        "Accesorio": "img_accesorio",
        "Complemento": "img_complemento",
    }

    columna_imagen = columnas_imagenes[nombre_con_prefijo]

    try:
        colecciones = obtener_colecciones()
        productos = obtener_productos()

        # Filtra colecciones y productos en memoria
        colecciones_filtradas = []
        for coleccion in colecciones:
            for producto in productos:
                if producto.tipo.lower() == nombre_con_prefijo.lower() and not coleccion.esta_eliminada and producto.coleccion_id == coleccion.id:
                    colecciones_filtradas.append({
                        "id": coleccion.id,
                        "nombre": coleccion.nombre,
                        "imgRepresentativa": getattr(coleccion, columna_imagen)
                    })
                    break

        return render_template('collection.html', colecciones_data=colecciones_filtradas, tipo=nombre_con_prefijo)

    except Exception as e:
        logger.error(f"Error al obtener base de datos: {e}")
        return "Error al obtener datos", 500


@index_blueprint.route('/nuestrodisenio/coleccion-buscada/<string:coleccion>')
def coleccionBuscada(coleccion):
    return render_template('collectionSearch.html', coleccion=coleccion)

@index_blueprint.route('/nuestrodisenio/coleccion/<string:nombre>/productmenu/<tipo>')
def productoMenuTipo(nombre, tipo):
    coleccion = obtener_coleccion_por_nombre(nombre)
    productos_info = obtener_producto_por_coleccion_y_tipo(coleccion.id, tipo)
    productos_encoded = json.dumps(productos_info, ensure_ascii=False)
    return render_template('productMenu.html', coleccion=coleccion, productos_info=productos_encoded)

@index_blueprint.route('/nuestrodisenio/coleccion/<string:nombre>/productmenu/<tipo>/product/<int:id>')
def productSelection(nombre, tipo, id):
    coleccion = obtener_coleccion_por_nombre(nombre)
    producto = obtener_producto_coleccion_tipo_id(coleccion.id, tipo, id)
    
    if producto is not None:
        return render_template('product.html', coleccion=coleccion, producto=producto)
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
        remitente_correo = 'infogriferiasthol@gmail.com'
        remitente_password = 'kxri prmp vfrn hhtz '
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
        print(f'Error en enviarCorreo: {e}')
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

    colecciones = obtener_colecciones()
    productos = obtener_productos()

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

    coincidencias_nombres_tipos = [coincidencia[0] for coincidencia in coincidencias if coincidencia[1] > 50]
    
    # Filtrar los productos que coinciden con los nombres y tipos
    productos_coincidentes = [
        producto for producto in nombres_productos 
        if (producto[1], producto[2]) in coincidencias_nombres_tipos
    ]

    # Usar el caché de colecciones para buscar coincidencias
    colecciones_coincidencias = [
        coleccion for coleccion in colecciones
        if coleccion.nombre.startswith(word)
    ]

    resultados_combinados = combinar_resultados(productos_coincidentes, colecciones_coincidencias)

    return jsonify(resultados_combinados)

