import { traerDistributors } from "../traerDistributors.js";
import { selectTBodyDistributors } from "../utils/constantes.js";
import { crearTableDistributors } from "../utils/crearFilaDistribuidores.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const distribuidores = await traerDistributors();
        crearTableDistributors(distribuidores, selectTBodyDistributors);

    } catch (error) {
        console.error('Error:', error);
    }
});