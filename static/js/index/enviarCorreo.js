btnEnviar = document.getElementById('btnConsultation')
btnEnviar.addEventListener('click', enviarCorreo)

async function enviarCorreo() {

    var nombre = document.querySelector('input[name="name"]').value;
    var asunto = document.querySelector('input[name="topic"]').value;
    var email = document.querySelector('input[name="email"]').value;
    var mensaje = document.querySelector('textarea[name="message"]').value;

    var consulta = {
        nombre: nombre,
        asunto: asunto,
        email: email,
        mensaje: mensaje
    };

    try {
        const response = await fetch('/enviarCorreo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(consulta)
        });

        console.log('Respuesta del servidor:', response);

    } catch (error) {

        console.error('Error al enviar la solicitud:', error);
    }
}