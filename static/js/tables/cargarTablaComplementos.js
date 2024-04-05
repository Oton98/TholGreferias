import { traerComplementos } from "../traerProducts.js";
import { selectTBodyAddons } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const complementos = await traerComplementos();
        crearTableRowProducts(complementos, selectTBodyAddons)

    } catch (error) {
        console.error('Error:', error);
    }
});