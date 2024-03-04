import { getIdFromURL } from "../utils/capturarIdUrl.js";
import { traerColeccion } from "../traerCollections.js";
import { traerTipoProducto } from "../traerProducts.js";
import { crearTarjetaMenuColecciones } from "../utils/crearMenuColeccion.js";

export async function cargarMenuColeccion(id, coleccionNombre) {
    
    const productosTipo = await traerTipoProducto(id);
    const productosTipoArray = productosTipo.productos;

    let containerTitulo = document.getElementById('containerTitle');
    let containerTarjetas = document.getElementById('containerCards');

    let titulo = document.createElement('h2');
    titulo.classList = "collection-container-title-text";
    titulo.innerText = coleccionNombre;
    
    containerTitulo.appendChild(titulo);
    
    // Utilizar un conjunto para almacenar tipos únicos
    const tiposUnicos = new Set();

    // Filtrar el array y agregar tipos únicos al conjunto
    productosTipoArray.forEach(producto => {
        tiposUnicos.add(producto.tipo);
    });

    // Iterar sobre tipos únicos y llamar a la función
    tiposUnicos.forEach(tipo => {
        crearTarjetaMenuColecciones(tipo, containerTarjetas, coleccionNombre);
        console.log(tipo)
    });

}
