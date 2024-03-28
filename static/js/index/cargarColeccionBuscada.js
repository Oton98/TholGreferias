import { crearTarjeta } from "../cards/crearTarjetaColeccionBuscada.js"

export function cargarColeccionBuscada(objetoProductos, coleccion) {
    let container = document.getElementById('collectionSearchedContainer');
    let secciones = {}; // Objeto para mantener las secciones por tipo de producto

    objetoProductos.productos.forEach(producto => {
        let tipo = producto.tipo;

        // Verificar si la sección ya ha sido creada para este tipo de producto
        if (!secciones[tipo]) {
            let seccion = document.createElement("section");
            seccion.classList = "colsearched-container-section";

            // Contenedor del título
            let tituloContainer = document.createElement("div");
            tituloContainer.classList = "colsearched-container-section-title";

            let titulo = document.createElement("h1");
            titulo.innerText = `Productos ${tipo}`;
            tituloContainer.appendChild(titulo);

            // Contenedor de las tarjetas
            let cardsContainer = document.createElement("div");
            cardsContainer.classList = "colsearched-container-section-cards";

            seccion.appendChild(tituloContainer);
            seccion.appendChild(cardsContainer);

            container.appendChild(seccion);
            secciones[tipo] = cardsContainer; // Guardar la referencia del contenedor de tarjetas
        }

        // Agregar tarjeta al tipo de producto correspondiente
        crearTarjeta(producto, coleccion, secciones[tipo]);
    });
}