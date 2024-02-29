import { traerColleciones } from "../traerCollections.js"
import { crearTarjetaColeccion } from "../utils/crearTarjetaColeccion.js";
window.addEventListener('DOMContentLoaded', cargarTarjetasColecciones)

async function cargarTarjetasColecciones() {
    try {
        var colecciones = await traerColleciones();
        var sectionContenedor = document.getElementById('collectionContainer');
        
        for (const coleccion of colecciones){
            const tarjeta = crearTarjetaColeccion(coleccion);
            sectionContenedor.appendChild(tarjeta);
        }

    } catch (error) {
        console.error('Error:', error.message);
        throw error;
    }

}

