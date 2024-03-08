export function crearTarjetasProductos(producto, containerTarjetas, coleccionNombre){

    let tarjeta = document.createElement('article');
    tarjeta.classList = "product-container-cards-card";

    let img = document.createElement('img');
    img.classList = "product-container-cards-card-img";

    let textDiv = document.createElement('div');
    textDiv.classList = "product-container-cards-card-text";
    let title = document.createElement('h4');
    title.classList = "product-container-cards-card-text-title";
    let url = document.createElement('a');
    url.classList = "product-container-cards-card-text-url";

    let urlProducto = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.tipo}/product/${producto.id}`;

    img.src = producto.imagen;
    title.innerText = producto.nombre;
    url.href = urlProducto;
    url.innerText = "Ver detalles del producto  >";
    
    textDiv.appendChild(title);
    textDiv.appendChild(url);

    tarjeta.appendChild(img);
    tarjeta.appendChild(textDiv);

    containerTarjetas.appendChild(tarjeta);

}