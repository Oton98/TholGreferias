export async function cargarMenuColeccion(nombre, imagen, tipo) {
    
    let containerTarjetas = document.getElementById('containerCards');
    let tarjeta = document.createElement('div');
    let imagenTarjeta = document.createElement('img');
    let tituloTarjeta = document.createElement('p');
    let aTag = document.createElement('a');
    let aTag2 = document.createElement('a');
    let textDiv = document.createElement('div');
    let textTarjeta = document.createElement('p');
    let link = `/nuestrodisenio/coleccion/${nombre}/productmenu/${tipo}`;1
    
    tarjeta.classList = "collection-container-cards-card";
    imagenTarjeta.classList = "collection-container-cards-card-img";
    textDiv.classList = "collection-container-cards-card-text";

    imagenTarjeta.src = imagen
    tituloTarjeta.innerText = nombre;
    textTarjeta.innerText = "Ver la colección completa >"
    aTag.href = link;
    aTag2.href = link;

    textDiv.appendChild(tituloTarjeta);
    textDiv.appendChild(textTarjeta);
    aTag.appendChild(textDiv);
    aTag2.appendChild(imagenTarjeta)
    
    tarjeta.appendChild(aTag2);
    tarjeta.appendChild(aTag);
    containerTarjetas.appendChild(tarjeta);

}
