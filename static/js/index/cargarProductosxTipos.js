import { crearTarjetasProductos } from "../cards/crearTarjetasProductos.js";

export async function cargarProductoxTipo(coleccionNombre, productos_info, tipoFiltrado) {

    let containerTitulo = document.getElementById('productTitle');
    let containerTarjetas = document.getElementById('productCards');

    let titulo = document.createElement('h2');
    titulo.classList = "product-container-title-text";
    titulo.innerText = "Colección " + coleccionNombre + " | " + tipoFiltrado + "s";
    
    containerTitulo.appendChild(titulo);
    
    productos_info.forEach(producto => {
        crearTarjetasProductos(producto, containerTarjetas, coleccionNombre);
    });
    
}
    
    
