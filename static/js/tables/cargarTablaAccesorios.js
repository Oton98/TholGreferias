import { traerAccesorios } from "../traerProducts.js";
import { selectTBodyAccesories } from "../utils/constantes.js";
import { crearTableRowProducts } from "../utils/crearFilaProductos.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const complementos = await traerAccesorios();
        crearTableRowProducts(complementos, selectTBodyAccesories())
        ordenarColumnaAlfabeticamente('coleccion', selectTBodyAccesories());

        const columnTitles = document.querySelectorAll('.title-head');
        columnTitles.forEach(title => {
            title.addEventListener('click', () => {
                const columnId = title.id;
                ordenarColumnaAlfabeticamente(columnId, selectTBodyAccesories());
            });
        });

    } catch (error) {
        console.error('Error:', error);
    }
});