import { traerDistributors } from "../traerDistributors.js";
import { obtenerProvinciasUnicas } from "./obtenerProvincias.js";
import { crearBotonesProvincia } from "./cargarMenuProvincias.js";
import { initMap } from "./googlemaps.js";

window.addEventListener('DOMContentLoaded', async () => {
    
    let provincias = await obtenerProvinciasUnicas();
    const distribuidores = await traerDistributors();

    crearBotonesProvincia(provincias, distribuidores);
    initMap();
});
