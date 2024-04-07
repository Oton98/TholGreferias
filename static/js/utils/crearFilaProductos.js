import { crearTableData } from "./crearTd.js";
import { crearCeldaBotones, crearTDimagen, crearPDFVisual } from "./crearTd.js";

const ordenColumnasProductos = [
    'nombre',
    'codigo',
    'coleccion',
    'tipo',
    'descripcion',
    'imagen',
    'colores',
    'manual',
    'medidas',
    'estaDisponible',
    'esDestacado'
];

export function crearTableRowProducts(productos, selectTBody) {
    for (const producto of productos) {
        var fila = document.createElement("tr");
        fila.classList = "table-tbody-tr";

        let medidas;
        let manual;
        let colores;
        let imagen;
        
        const celdaBotones = crearCeldaBotones(producto.id, "productos/deleteProduct");

        for (const clave of ordenColumnasProductos) {
            if (clave !== 'id') {
                // Si la clave es imagen, descripción, colores, manual o medidas
                switch (clave) {
                    case 'imagen':
                        imagen = producto[clave];
                        crearTDimagen(imagen, fila);
                        break;
                    case 'colores':
                        colores = producto[clave];
                        crearTDimagen(colores, fila);
                        break;
                    case 'manual':
                        manual = producto[clave];
                        crearPDFVisual(manual, fila);
                        break;
                    case 'medidas':
                        medidas = producto[clave];
                        crearPDFVisual(medidas, fila);
                        break;
                    default:
                        const valor = producto[clave];
                        crearTableData(valor, fila, clave); // Pasar el identificador de la columna a crearTableData
                }
            }
        }

        fila.appendChild(celdaBotones);
        selectTBody.appendChild(fila);
    }
}