const btnActualizar = document.getElementById('updateProduct');
const form = document.querySelector('.control-panelbox-form form');

btnActualizar.addEventListener('click', function () {
    var idProducto = form.id;
    modificar(idProducto);
})

async function modificar(id) {

    var nombreNuevo = document.getElementById('productName').value;
    var codigoNuevo = document.getElementById('productCode').value;
    var tipoNuevo = document.getElementById('productType').value;
    var coleccionNuevo = document.getElementById('collection').value
    var descripcionNuevo = document.getElementById('descriptionProduct').value;
    var imagenNuevo = document.getElementById('productImage').value;
    var coloresNuevo = document.getElementById('productColores').value;
    var medidasNuevo = document.getElementById('collectionManualDetails').value;
    var manualNuevo = document.getElementById('collectionManualInstalation').value;
    var esDestacadoNuevo = document.getElementById('isFeaturedProducto').checked;
    var estaDisponibleNuevo = document.getElementById('isAvailable').checked;
    
    var productoNuevo = {

        nombre: nombreNuevo,
        codigo: codigoNuevo,
        tipo: tipoNuevo,
        coleccion: coleccionNuevo,
        descripcion: descripcionNuevo,
        imagen: imagenNuevo,
        colores: coloresNuevo,
        medidas: medidasNuevo,
        manual: manualNuevo,
        estaDisponible: estaDisponibleNuevo,
        esDestacado: esDestacadoNuevo

    }
    
    try {
        // Enviar la solicitud PUT con await
        const response = await fetch('/updateProduct/' + id, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productoNuevo),
        });

        // Manejar la respuesta del servidor
        const data = await response.json();
        console.log('Respuesta del servidor:', data);

        // Puedes realizar operaciones adicionales aquí si es necesario
    } catch (error) {
        console.error('Error al enviar la solicitud:', error);
    }
}
