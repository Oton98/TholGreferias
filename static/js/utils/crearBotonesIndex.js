export function crearBotonesIndex(texto, icono, url) {

    let reference = document.createElement('a');
    reference.href = url;

    let icon = document.createElement('span');
    icon.classList = "material-symbols-outlined";
    icon.innerText = icono;

    let text = document.createElement('p');
    text.innerText = texto;

    reference.appendChild(icon);
    reference.appendChild(text);

    return reference;
}