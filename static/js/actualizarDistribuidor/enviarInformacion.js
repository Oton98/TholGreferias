export async function enviarInformacion(id) {
    const valorNombre = document.getElementById('DistributorName').value;
    const valorDireccion = document.getElementById('DistributorAdress').value
    const valorRegion = document.getElementById('ProvinciaAdress').value;
    const valorLatitud = document.getElementById('DistributorLatitude').value;
    const valorLongitud = document.getElementById('DistributorLength').value;
    const valorWeb = document.getElementById('DistributorWeb').value;
    const valorWhatsapp = document.getElementById('DistributorWhatsapp').value;
    const valorTelefono = document.getElementById('DistributorPhone').value;

    let distribuidorActualizado = {
        nombre: valorNombre,
        direccion: valorDireccion,
        region: valorRegion,
        latitud: valorLatitud,
        longitud: valorLongitud,
        web: valorWeb,
        whatsapp: valorWhatsapp,
        telefono: valorTelefono
    }

    try {
        const response = await fetch('/distribuidores/updatedistributor/' + id, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(distribuidorActualizado),
        });

        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.statusText}`);
        }

        const data = await response.json();


        setTimeout(() => {
            window.location.reload();
        }, 1000);

        alert(data.message + '. Toca "Aceptar" para continuar');


    } catch (error) {
        console.error('Error al enviar la solicitud:', error);
    }

} 