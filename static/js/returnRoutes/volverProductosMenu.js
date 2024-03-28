export function crearRutaProductoMenuVolver(tipo) {
    let contenedor = document.getElementById('productRoute');
    console.log(tipo)
    let linkAtras = document.createElement('a');
    linkAtras.classList = "product-container-route-link";
    let textAtras = document.createElement('p');
    textAtras.classList = "product-container-route-text"

    let iconBackTag = document.createElement('span');
    iconBackTag.classList = "material-symbols-outlined product-container-route-link-icon ";
    iconBackTag.innerText = "keyboard_backspace";

    linkAtras.appendChild(iconBackTag);

    textAtras.appendChild(linkAtras);
    textAtras.innerText = "Volver";
    linkAtras.href = `/nuestrodisenio/coleccion/${tipo}`;
    linkAtras.appendChild(textAtras);

    let linkCompleto = document.createElement('a');
    // Falta crear link completo

    contenedor.appendChild(linkAtras);
    // contenedor.appendChild(linkCompleto);
}