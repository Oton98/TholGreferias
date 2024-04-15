export function crearTarjetasProductosDestacados(producto, containerTarjetas, coleccionNombre){

    let tarjeta = document.createElement('article');
    tarjeta.classList = "featured-products-container-cards-card";

    let img = document.createElement('img');
    img.classList = "featured-products-container-cards-card-img";

    let textDiv = document.createElement('div');
    textDiv.classList = "featured-products-container-cards-card-text";
    let title = document.createElement('h4');
    title.classList = "featured-products-container-cards-card-text-title";
    let text = document.createElement('p');
    title.classList = "featured-products-container-cards-card-text-description"
    let url = document.createElement('a');
    url.classList = "featured-products-container-cards-card-text-url";
    let url2 = document.createElement('a');
    url.classList = "featured-products-container-cards-card-text-url";

    let urlProducto = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.tipo}/product/${producto.id}`;

    img.src = producto.imagen;
    title.innerText = `${coleccionNombre} ${producto.nombre}`;
    url2.href = urlProducto;
    url.href = urlProducto;
    text.innerText = "Ver detalles del producto  >";
    
    textDiv.appendChild(title);
    textDiv.appendChild(text);

    url.appendChild(img);
    url2.appendChild(textDiv);

    tarjeta.appendChild(url);
    tarjeta.appendChild(url2);

    containerTarjetas.appendChild(tarjeta);

}