import { traerGriferias } from "../traerProducts.js";
import { selectTBodyFaucets } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";
import { ordenarColumnaAlfabeticamente } from "./ordenarAlfabeticamente.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const griferias = await traerGriferias();
        crearTableRowProducts(griferias, selectTBodyFaucets);
        ordenarColumnaAlfabeticamente('coleccion');

        // Agregar eventos de clic a los títulos de columna
        const columnTitles = document.querySelectorAll('.title-head');
        columnTitles.forEach(title => {
            title.addEventListener('click', () => {
                const columnId = title.id;
                ordenarColumnaAlfabeticamente(columnId);
            });
        });
    } catch (error) {
        console.error('Error:', error);
    }
});