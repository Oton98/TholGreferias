export function crearBotonesIndex(texto, clase, url) {

    let reference = document.createElement('a')
    reference.href = url

    let button = document.createElement('button');
    button.innerText = texto;
    button.classList = clase;

    reference.appendChild(button);

    return reference;
}