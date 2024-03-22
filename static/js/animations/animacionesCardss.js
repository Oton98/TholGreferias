export function agregarEventosHover(claseContenedor, claseTexto) {
    
    claseContenedor.forEach(card => {
        const title = card.querySelector(claseTexto);

        card.addEventListener('mouseover', () => {
            title.classList.add('hovered');
        });

        card.addEventListener('mouseout', () => {
            title.classList.remove('hovered');
        });
    });
}

export function agregaEventosClick(claseContenedor, claseTexto) {
    claseContenedor.forEach(card => {
        const title = card.querySelector(claseTexto);

        card.addEventListener('mousedown', () => {
            title.classList.add('clicked'); 
        });

        card.addEventListener('mouseup', () => {
            title.classList.remove('clicked'); 
        });

        card.addEventListener('mouseleave', () => {
            title.classList.remove('clicked'); 
        });
    });
}

