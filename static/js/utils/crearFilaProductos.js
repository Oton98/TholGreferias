import { crearTableData } from "./crearTd.js";
import { crearCeldaBotones } from "./crearTd.js";

const ordenColumnasProductos = [
    'nombre',
    'codigo',
    'coleccion',
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

        const celdaBotones = crearCeldaBotones(producto.id);
        
        for (const clave of ordenColumnasProductos) {
            if (clave !== 'id') {
                const valor = producto[clave];
                
                crearTableData(valor, fila);

            }
        }

        fila.appendChild(celdaBotones);
        selectTBody.appendChild(fila);
    }
}
