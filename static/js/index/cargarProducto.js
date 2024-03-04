import { cargarPantallaProducto } from "../cards/crearPantallaProducto.js";

export function cargarProducto(coleccionNombre, productosDeLaColeccion, producto){
    let containerTitulo = document.getElementById('productTitle');
    let containerTarjeta = document.getElementById('productCardContainer');

    let titulo = document.createElement('h2');
    titulo.classList = "product-type-container-title-text";
    titulo.innerText = coleccionNombre;
    
    containerTitulo.appendChild(titulo);
    cargarPantallaProducto(productosDeLaColeccion, producto, containerTarjeta);


}