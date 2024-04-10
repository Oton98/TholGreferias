import { traerDistributor } from "../traerDistributors.js";

export async function cargarDatosDistribuidor(id) {
    try {
        const form = document.querySelector('.control-panelbox-form form');
        form.id = id;
        
        const distribuidor = await traerDistributor(id);

        if (distribuidor) {
            document.getElementById('DistributorName').value = distribuidor.nombre;
            document.getElementById('DistributorAdress').value = distribuidor.Dirección;
            document.getElementById('ProvinciaAdress').value = distribuidor.Localidad;
            document.getElementById('DistributorLatitude').value = distribuidor.latitud;
            document.getElementById('DistributorLength').value = distribuidor.longitud;
            document.getElementById('DistributorWeb').value = distribuidor.Web;
            document.getElementById('DistributorWhatsapp').value = distribuidor.Whatsapp;
            document.getElementById('DistributorPhone').value =  distribuidor.Teléfono;
        } else {
            throw new Error('Distribuidor no encontrado');
        }
    } catch (error) {
        throw new Error('Error al cargar datos del distribuidor:', error);
    }
}