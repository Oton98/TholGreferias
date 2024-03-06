export function crearTarjetasProductos(producto, containerTarjetas, coleccionNombre){

    let tarjeta = document.createElement('article');
    tarjeta.classList = "product-type-container-cards-card";

    let img = document.createElement('img');
    img.classList = "product-type-container-cards-card-img"

    let textDiv = document.createElement('div');
    textDiv.classList = "product-type-container-cards-card-text"
    let title = document.createElement('h4');
    title.classList = "product-type-container-cards-card-text-title"
    let url = document.createElement('a');
    url.classList = "product-type-container-cards-card-text-url"

    let urlProducto = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.productoTipo}/product/${producto.id}`;

    img.src = producto.imagenProducto
    console.log(img)
    title.innerText = producto.nombre
    url.href = urlProducto
    url.innerText = "Ver la colección completa  >"
    
    textDiv.appendChild(title);
    textDiv.appendChild(url);

    tarjeta.appendChild(img);
    tarjeta.appendChild(textDiv);

    containerTarjetas.appendChild(tarjeta);

}