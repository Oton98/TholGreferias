import { traerProductoDestacados } from "../traerProducts.js";
import { crearTarjetasProductosDestacados } from "../cards/crearTarjetaProductoDestacado.js";

window.addEventListener('DOMContentLoaded', async () => {
    const productosDestacados = await traerProductoDestacados();
    let contenedor = document.getElementById('featuredProducts');

    productosDestacados.forEach(producto => {
        const nombreColeccion = producto.coleccion;
        crearTarjetasProductosDestacados(producto, contenedor, nombreColeccion);
    });
});