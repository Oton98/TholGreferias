import { mezclarArray } from "../utils/crearArrayRandom.js";
import { traerColeccion } from "../traerCollections.js";
import {agregaEventosClick, agregarEventosHover} from "../animations/animacionesCardss.js"

export async function tarjetaProductosRelacionados(contenedorProductosRelacionados, productosDeLaColeccion, productoId) {

    const productosColeccion = productosDeLaColeccion.productos;
    mezclarArray(productosColeccion, productoId);
    const productosSeleccionados = productosColeccion.slice(0, 5);

    for (const producto of productosSeleccionados) {
        let productoRelacionado = document.createElement('article');
        productoRelacionado.classList = "relationed-product-container-cards-card";

        let imagenProductoRelacionado = document.createElement('img');
        imagenProductoRelacionado.classList  = "relationed-product-container-cards-card-img";
        imagenProductoRelacionado.src = producto.imagen;

        let nombreProductoRelacionado = document.createElement('h4');
        nombreProductoRelacionado.classList  = "relationed-product-container-cards-card-text";
        nombreProductoRelacionado.innerText = producto.nombre;

        try {
            let coleccion = await traerColeccion(producto.coleccion);

            let link = document.createElement('a');
            let link2 = document.createElement('a');
            link.href = `/nuestrodisenio/coleccion/${coleccion.nombre}/productmenu/${producto.tipo}/product/${producto.id}`;
            link2.href = `/nuestrodisenio/coleccion/${coleccion.nombre}/productmenu/${producto.tipo}/product/${producto.id}`;
            
            link.appendChild(imagenProductoRelacionado);
            link2.appendChild(nombreProductoRelacionado);

            productoRelacionado.appendChild(link);
            productoRelacionado.appendChild(link2);
            contenedorProductosRelacionados.appendChild(productoRelacionado);

        } catch (error) {
            console.error("Error al obtener información de la colección", error);
        }
    }

    let cartas = document.querySelectorAll(".relationed-product-container-cards-card");
    agregaEventosClick(cartas, ".relationed-product-container-cards-card-text");
    agregarEventosHover(cartas, ".relationed-product-container-cards-card-text");


}