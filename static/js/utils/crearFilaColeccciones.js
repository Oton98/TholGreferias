import {crearTableData} from "./crearTd.js"

const ordenColumnasColeccion = [
    'nombre',
    'cant_Products',
    'productos'
];

export function crearTableCollections(productos, selectTBody) {
    for (const producto of productos) {
        var fila = document.createElement("tr");

        for (const clave of ordenColumnasColeccion) {
            if (clave !== 'id') {
                const valor = producto[clave];
                
                if (clave === 'productos' && Array.isArray(valor) && valor.length > 0) {
                    const nombresProductos = valor.map(productoInterno => productoInterno.nombre_producto).join(', ');
                    crearTableData(nombresProductos, fila);
                } else {
                    crearTableData(valor, fila);
                }
            }
        }

        selectTBody.appendChild(fila);
    }
}