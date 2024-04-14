import { crearTableData } from "./crearTd.js"
import { crearCeldaBotones, crearTDimagen } from "./crearTd.js";

const ordenColumnasColeccion = [
    'nombre',
    'imgBimando',
    'imgMonocomando',
    'imgFreestanding',
    'imgComplemento',
    'imgAccesorio',
    'cant_Products',
    'productos',
];

export function crearTableCollections(colecciones, selectTBody) {
    for (const coleccion of colecciones) {
        var fila = document.createElement("tr");
        fila.classList = "table-tbody-tr";
        const celdaBotones = crearCeldaBotones(coleccion.id, "colecciones/deleteCollection");

        for (const clave of ordenColumnasColeccion) {
            if (clave !== 'id') {
                const valor = coleccion[clave];

                if (clave === 'productos' && Array.isArray(valor) && valor.length > 0) {
                    const nombresProductos = valor.map(productoInterno => productoInterno.nombre_producto).join(', ');
                    crearTableData(nombresProductos, fila);
                } else if (['imgBimando', 'imgMonocomando', 'imgFreestanding', 'imgComplemento', 'imgAccesorio'].includes(clave)) {
                    crearTDimagen(valor, fila);
                } else {
                    crearTableData(valor, fila);
                }
            }
        }

        fila.appendChild(celdaBotones);
        selectTBody.appendChild(fila);
    }
}