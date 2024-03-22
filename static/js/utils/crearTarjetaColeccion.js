export function crearTarjetaColeccion(tipo, link){

    var contenedor = document.createElement('article');
    var divTarjetConentedor = document.createElement('div');

    var linkTarjeta = document.createElement('a');
    var linkTarjeta2= document.createElement('a');
    
    var imgTarjeta = document.createElement('img');
    var tituloTarjeta = document.createElement('h4');

    contenedor.classList = "collections-body-container-card";
    imgTarjeta.classList = "collections-body-container-card-text-link-img";
    divTarjetConentedor.classList = "collections-body-container-card-text";
    tituloTarjeta.classList = "collections-body-container-card-text-link-title";
    linkTarjeta.classList = "collections-body-container-card-text-link";

    const nombreColeccion = tipo;
    const imagenColeccion = link;
    var linkColeccion = `nuestrodisenio/coleccion/${tipo}`;

    tituloTarjeta.innerText = nombreColeccion;
    imgTarjeta.src = imagenColeccion;
    linkTarjeta.href = linkColeccion;
    linkTarjeta.innerText = ""
    linkTarjeta2.href = linkColeccion;

    linkTarjeta.appendChild(imgTarjeta);
    linkTarjeta2.appendChild(tituloTarjeta);

    divTarjetConentedor.appendChild(linkTarjeta);
    divTarjetConentedor.appendChild(linkTarjeta2);

    contenedor.appendChild(divTarjetConentedor);

    return contenedor

}