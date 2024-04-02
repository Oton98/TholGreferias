import { crearTableData } from "./crearTd.js"
import { crearCeldaBotones } from "./crearTd.js";

const ordenColumnasDistribuidores = [
    'nombre',
    'direccion',
    'provincia',
    'latitud',
    'longitud',
];


export function crearTableDistributors(distribuidores, selectTBody) {
    for (const distribuidor of distribuidores) {
        console.log(distribuidor)
        var fila = document.createElement("tr");
        fila.classList = "table-tbody-tr";
        const celdaBotones = crearCeldaBotones(distribuidor.id, "distribuidores/delatedistributor");

        for (const clave of ordenColumnasDistribuidores) {
            if (clave !== 'id') {
                const valor = distribuidor[clave];
                console.log(distribuidor[clave])
                crearTableData(valor, fila);
            }
        }

        fila.appendChild(celdaBotones);
        selectTBody.appendChild(fila);
    }
}