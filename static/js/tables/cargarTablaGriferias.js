import { traerGriferias } from "../traerProducts.js";
import { selectTBodyFaucets } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const griferias = await traerGriferias();
        crearTableRowProducts(griferias, selectTBodyFaucets)

    } catch (error) {
        console.error('Error:', error);
    }
});