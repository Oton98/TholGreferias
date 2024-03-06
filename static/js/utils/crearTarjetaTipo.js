export function crearTarjetaTipo(imagen, link) {

    let tarjeta = document.createElement('div');
    tarjeta.classList = "collection-container-cards-card";

    let imagenTarjeta = document.createElement('img');
    imagenTarjeta.classList = "collection-container-cards-card-img"
    imagenTarjeta.src = imagen
    
    let text = document.createElement('a');
    text.classList = "collection-container-cards-card-text"
    text.href = link;
    text.innerText = "Ver todos los productos >";

    tarjeta.appendChild(imagenTarjeta);
    tarjeta.appendChild(text);

    return tarjeta
}