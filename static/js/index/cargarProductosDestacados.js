import { traerProductoDestacados } from "../traerProducts.js";
import { crearTarjetasProductosDestacados } from "../cards/crearTarjetaProductoDestacado.js";
import { agregarEventosHover, agregaEventosClick } from '../animations/animacionesCardss.js';

window.addEventListener('DOMContentLoaded', async () => {
    const productosDestacados = await traerProductoDestacados();
    let contenedor = document.getElementById('featuredProducts');

    productosDestacados.forEach(producto => {
        const nombreColeccion = producto.coleccion;
        crearTarjetasProductosDestacados(producto, contenedor, nombreColeccion);
        let cartas = document.querySelectorAll(".featured-products-container-cards-card");
        agregaEventosClick(cartas, ".featured-products-container-cards-card-text");
        agregarEventosHover(cartas, ".featured-products-container-cards-card-text");
    });
});