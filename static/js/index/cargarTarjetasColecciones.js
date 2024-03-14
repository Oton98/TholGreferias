import { traerColleciones } from "../traerCollections.js"
import { tipoTarjetasImg, tipoTarjetasNombre } from "../utils/constantes.js";
import { crearTarjetaColeccion } from "../utils/crearTarjetaColeccion.js";
window.addEventListener('DOMContentLoaded', cargarTarjetasColecciones)

async function cargarTarjetasColecciones() {

    var sectionContenedor = document.getElementById('collectionContainer');

    for (let i = 0; i < tipoTarjetasImg.length; i++) {
        const tarjeta = crearTarjetaColeccion(tipoTarjetasNombre[i],tipoTarjetasImg[i]);
        sectionContenedor.appendChild(tarjeta);
    }
    
}

