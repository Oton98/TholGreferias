import { traerDistributors } from "../traerDistributors.js"; 

export async function obtenerProvinciasUnicas() {
    const distribuidores = await traerDistributors();
    const provinciasUnicas = [];
    const provinciasMap = {};

    distribuidores.forEach(distribuidor => {
        const provincia = distribuidor.Localidad;

        if (!provinciasMap[provincia]) {
            provinciasMap[provincia] = true;
            provinciasUnicas.push(provincia);
        }
    });
    return provinciasUnicas;
}
