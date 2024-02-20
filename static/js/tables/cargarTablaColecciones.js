import { traerColleciones } from "../traerCollections.js";
import { selectTBodyCollections } from "../utils/constantes.js";
import { crearTableCollections } from "../utils/crearFilaColeccciones.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const colecciones = await traerColleciones();
        crearTableCollections(colecciones, selectTBodyCollections);
    } catch (error) {
        console.error('Error:', error);
    }
});