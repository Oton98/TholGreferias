export function crearTarjetasProductosDestacados(producto, containerTarjetas, coleccionNombre){

    let tarjeta = document.createElement('article');
    tarjeta.classList = "featured-products-container-cards-card";

    let img = document.createElement('img');
    img.classList = "featured-products-container-cards-card-img";

    let textDiv = document.createElement('div');
    textDiv.classList = "featured-products-container-cards-card-text";
    let title = document.createElement('h4');
    title.classList = "featured-products-container-cards-card-text-title";
    let url = document.createElement('a');
    url.classList = "featured-products-container-cards-card-text-url";

    let urlProducto = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.tipo}/product/${producto.id}`;

    img.src = producto.imagen;
    title.innerText = `${coleccionNombre} ${producto.nombre}`;
    url.href = urlProducto;
    url.innerText = "Ver detalles del producto  >";
    
    textDiv.appendChild(title);
    textDiv.appendChild(url);

    tarjeta.appendChild(img);
    tarjeta.appendChild(textDiv);

    containerTarjetas.appendChild(tarjeta);

}