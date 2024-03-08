import { crearTarjetasProductos } from "../cards/crearTarjetasProductos.js";

export async function cargarProductoxTipo(coleccionNombre, productos_info) {

    let containerTitulo = document.getElementById('productTitle');
    let containerTarjetas = document.getElementById('productCards');

    let titulo = document.createElement('h2');
    titulo.classList = "product-container-title-text";
    titulo.innerText = coleccionNombre;
    
    containerTitulo.appendChild(titulo);
    
    productos_info.forEach(producto => {
        crearTarjetasProductos(producto, containerTarjetas, coleccionNombre);
    });
    
}
    
    
