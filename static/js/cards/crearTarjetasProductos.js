export function crearTarjetasProductos(producto, containerTarjetas, coleccionNombre){

    let tarjeta = document.createElement('article');
    tarjeta.classList = "product-type-container-cards-card";

    let img = document.createElement('img');
    img.classList = "product-type-container-cards-card-img"
    let title = document.createElement('h4');
    title.classList = "product-type-container-cards-card-title"
    let url = document.createElement('a');
    url.classList = "product-type-container-cards-card-url"

    let urlProducto = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${producto.productoTipo}/product/${producto.id}`;

    img.src = producto.imagenProducto
    console.log(img)
    title.innerText = producto.nombre
    url.href = urlProducto
    url.innerText = "Ver la colección completa  >"
    

    tarjeta.appendChild(img);
    tarjeta.appendChild(title);
    tarjeta.appendChild(url);

    containerTarjetas.appendChild(tarjeta);

}