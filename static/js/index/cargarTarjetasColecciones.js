import { tipoTarjetasImg, tipoTarjetasNombre } from "../utils/constantes.js";
import { crearTarjetaColeccion } from "../utils/crearTarjetaColeccion.js";
import { agregarEventosHover, agregaEventosClick} from "../animations/animacionesCardss.js";

window.addEventListener('DOMContentLoaded', async () => {
    await cargarTarjetasColecciones();
    let cartas = document.querySelectorAll('.collections-body-container-card');
    agregarEventosHover(cartas, '.collections-body-container-card-text-link-title');
    agregaEventosClick(cartas, '.collections-body-container-card-text-link-title');
});

async function cargarTarjetasColecciones() {
    var sectionContenedor = document.getElementById('collectionContainer');

    for (let i = 0; i < tipoTarjetasImg.length; i++) {
        const tarjeta = crearTarjetaColeccion(tipoTarjetasNombre[i], tipoTarjetasImg[i]);
        sectionContenedor.appendChild(tarjeta);
    }
    
}


