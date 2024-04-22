export function agregarEventosHover(claseCarta, claseTexto) {
    claseCarta.forEach(card => {
        const textElement = card.querySelector(claseTexto);

        card.addEventListener('mouseover', () => {
            card.classList.add('hovered');
            textElement.classList.add('hovered');
        });

        card.addEventListener('mouseout', () => {
            card.classList.remove('hovered');
            textElement.classList.remove('hovered');
        });
    });
}

export function agregaEventosClick(claseCarta, claseTexto) {
    claseCarta.forEach(card => {
        const textElement = card.querySelector(claseTexto);

        card.addEventListener('mousedown', () => {
            card.classList.add('clicked');
            textElement.classList.add('clicked');
        });

        card.addEventListener('mouseup', () => {
            card.classList.remove('clicked');
            textElement.classList.remove('clicked');
        });

        card.addEventListener('mouseleave', () => {
            card.classList.remove('clicked');
            textElement.classList.remove('clicked');
        });
    });
}
