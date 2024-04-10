import { crearTableData } from "./crearTd.js"
import { crearCeldaBotones } from "./crearTd.js";

const ordenColumnasDistribuidores = [
    'nombre',
    'Dirección',
    'Localidad',
    'latitud',
    'longitud',
    'Web',
    'Whatsapp',
    'Teléfono',
];


export function crearTableDistributors(distribuidores, selectTBody) {
    for (const distribuidor of distribuidores) {
        var fila = document.createElement("tr");
        fila.classList = "table-tbody-tr";
        const celdaBotones = crearCeldaBotones(distribuidor.id, "distribuidores/delatedistributor");

        for (const clave of ordenColumnasDistribuidores) {
            if (clave !== 'id') {
                const valor = distribuidor[clave];
                crearTableData(valor, fila);
            }
        }

        fila.appendChild(celdaBotones);
        selectTBody.appendChild(fila);
    }
}