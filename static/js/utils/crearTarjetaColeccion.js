export function crearTarjetaColeccion(tipo, link){

    var contenedor = document.createElement('article');
    var divTarjetConentedor = document.createElement('div');
    var imgTarjeta = document.createElement('img');
    var tituloTarjeta = document.createElement('h4');
    var linkTarjeta = document.createElement('a');

    contenedor.classList = "collections-body-container-card"
    imgTarjeta.classList = "collections-body-container-card-img"
    divTarjetConentedor.classList = "collections-body-container-card-text"
    tituloTarjeta.classList = "collections-body-container-card-text-title"
    linkTarjeta.classList = "collections-body-container-card-text-link"

    const nombreColeccion = tipo;
    const imagenColeccion = link;
    var linkColeccion = `nuestrodisenio/coleccion/${tipo}`;

    tituloTarjeta.innerText = nombreColeccion;
    imgTarjeta.src = imagenColeccion;
    linkTarjeta.href = linkColeccion;
    linkTarjeta.innerText = "Ver categoría >"

    divTarjetConentedor.appendChild(tituloTarjeta);
    divTarjetConentedor.appendChild(linkTarjeta);

    contenedor.appendChild(imgTarjeta);
    contenedor.appendChild(divTarjetConentedor);

    return contenedor

}