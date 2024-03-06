import { mezclarArray } from "../utils/crearArrayRandom.js";
import { traerColeccion } from "../traerCollections.js";

export async function tarjetaProductosRelacionados(contenedorProductosRelacionados, productosDeLaColeccion, productoId) {

    const productosColeccion = productosDeLaColeccion.productos; 
    mezclarArray(productosColeccion, productoId);
    const productosSeleccionados = productosColeccion.slice(0, 5);

    for (const producto of productosSeleccionados) {
        let productoRelacionado = document.createElement('article');
        productoRelacionado.className = "relationed-product-container-cards-card";

        let imagenProductoRelacionado = document.createElement('img');
        imagenProductoRelacionado.className = "relationed-product-container-cards-card-img";
        imagenProductoRelacionado.src = producto.imagen;

        let nombreProductoRelacionado = document.createElement('h4');
        nombreProductoRelacionado.className = "relationed-product-container-cards-card-title";
        nombreProductoRelacionado.innerText = producto.nombre;

        try {
            let coleccion = await traerColeccion(producto.coleccion);

            let link = document.createElement('a');
            link.href = `/nuestrodisenio/coleccion/${coleccion.nombre}/productmenu/${producto.tipo}/product/${producto.id}`;

            link.appendChild(nombreProductoRelacionado)
            productoRelacionado.appendChild(imagenProductoRelacionado);
            productoRelacionado.appendChild(link);
            contenedorProductosRelacionados.appendChild(productoRelacionado);

        } catch (error) {
            console.error("Error al obtener información de la colección", error);
        }
    }
}