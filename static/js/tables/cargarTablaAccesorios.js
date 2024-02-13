import { traerAccesorios } from "../traerProducts.js";
import { selectTBodyAccesories } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const complementos = await traerAccesorios();
        crearTableRowProducts(complementos, selectTBodyAccesories)

    } catch (error) {
        console.error('Error:', error);
    }
});