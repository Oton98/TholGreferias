from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask import Blueprint, jsonify, render_template, request

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')

@index_blueprint.route('/index')
def index():
    return render_template('index.html')

@index_blueprint.route('/nuestroDiseño')
def nuestroDisenio():
    return render_template('nuestroDisenio.html')

@index_blueprint.route('/puntosDeVenta')
def puntosDeVenta():
    return render_template('puntosDeVenta.html')

@index_blueprint.route('/personalizacion')
def personalizacion():
    return render_template('personalizacion.html')

@index_blueprint.route('/consulta')
def consulta():
    return render_template('consulta.html')

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
