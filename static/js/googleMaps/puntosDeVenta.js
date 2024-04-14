import { traerDistributors } from "../traerDistributors.js";
import { obtenerProvinciasUnicas } from "./obtenerProvincias.js";
import { crearBotonesProvincia } from "./cargarMenuProvincias.js";
import { initMap } from "./googlemaps.js";
import { animacionDistribuidores } from "../animations/animacionesDistribuidores.js";

window.addEventListener('DOMContentLoaded', async () => {

    //Crear botones de provicias/regiones
    let provincias = await obtenerProvinciasUnicas();
    const distribuidores = await traerDistributors();
    crearBotonesProvincia(provincias, distribuidores);

    //Agregarles las animaciones
    const regiones = document.querySelectorAll(".partnership-locations-regions");
    const regionContainers = document.querySelectorAll(".partnership-locations-regions-cityTitle h3");
    animacionDistribuidores(regiones, regionContainers);
    
    //Cargar Mapa
    initMap();
});
