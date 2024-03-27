export function cargarTituloProducto(tipo) {
    let titulo = document.createElement('h1');
    let container = document.getElementById('containerTitle');
    
    switch (tipo) {
        case ("Grifería Monocomando"):
            titulo.innerText = "Conocé nuestras colecciones de griferías Monocomando";
            container.appendChild(titulo);
            break
        case ("Grifería Bimando"):
            titulo.innerText = "Conocé nuestras colecciones de griferías Bimando";
            container.appendChild(titulo);
            break
        case ("Grifería Freestanding"):
            titulo.innerText = "Conocé nuestras colecciones de griferías Freestanding";
            container.appendChild(titulo);
            break
        case ("Complemento"):
            titulo.innerText = "Conocé nuestras colecciones de Complementos";
            container.appendChild(titulo);
            break
        case ("Accesorio"):
            titulo.innerText = "Conocé nuestras colecciones de Accesorios";
            container.appendChild(titulo);
            break
    }

}