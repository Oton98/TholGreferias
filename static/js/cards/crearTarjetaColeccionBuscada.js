export function crearTarjeta(producto, coleccionNombre, containerTarjetas){
    let tarjeta = document.createElement('article');
    let imagenTarjeta = document.createElement('img');
    let tituloTarjeta = document.createElement('p');
    let aTag = document.createElement('a');
    let aTag2 = document.createElement('a');
    let textDiv = document.createElement('div');
    let textTarjeta = document.createElement('p');
    let link = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.tipo}/product/${producto.id}`;

    tarjeta.classList = "colsearched-container-section-cards-card";
    imagenTarjeta.classList = "colsearched-container-section-cards-card-img";
    textDiv.classList = "colsearched-container-section-cards-card-text";

    imagenTarjeta.src = producto.imagen;
    tituloTarjeta.innerText = producto.nombre;
    textTarjeta.innerText = "Ver detalles del producto  >";
    aTag.href = link;
    aTag2.href = link;

    textDiv.appendChild(tituloTarjeta);
    textDiv.appendChild(textTarjeta);
    aTag.appendChild(textDiv);
    aTag2.appendChild(imagenTarjeta);
    
    tarjeta.appendChild(aTag2);
    tarjeta.appendChild(aTag);

    containerTarjetas.appendChild(tarjeta);
}