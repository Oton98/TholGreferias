import { crearTarjetasProductos } from "../cards/crearTarjetasProductos.js";

export async function cargarProductoxTipo(coleccionNombre, productos_info) {

    let containerTitulo = document.getElementById('productTypeTitle');
    let containerTarjetas = document.getElementById('productTypeCards');

    let titulo = document.createElement('h2');
    titulo.classList = "product-type-container-title-text";
    titulo.innerText = coleccionNombre;
    
    containerTitulo.appendChild(titulo);

    productos_info.forEach(producto => {
        crearTarjetasProductos(producto, containerTarjetas, coleccionNombre);
    });
    
}
    
    
