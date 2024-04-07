import { traerComplementos } from "../traerProducts.js";
import { selectTBodyAddons } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";
import { ordenarColumnaAlfabeticamente } from "./ordenarAlfabeticamente.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const complementos = await traerComplementos();
        crearTableRowProducts(complementos, selectTBodyAddons())
        ordenarColumnaAlfabeticamente('coleccion', selectTBodyAddons());

        // Agregar eventos de clic a los títulos de columna
        const columnTitles = document.querySelectorAll('.title-head');
        columnTitles.forEach(title => {
            title.addEventListener('click', () => {
                const columnId = title.id;
                ordenarColumnaAlfabeticamente(columnId, selectTBodyAddons());
            });
        });

    } catch (error) {
        console.error('Error:', error);
    }
});