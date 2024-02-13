import { traerColleciones } from "../traerProducts.js";
import { selectTBodyCollections } from "../utils/constantes.js";
import { crearTableCollections } from "../utils/crearFilaColeccciones.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const complementos = await traerColleciones();
        crearTableCollections(complementos, selectTBodyCollections);
        console.log(complementos);

    } catch (error) {
        console.error('Error:', error);
    }
});