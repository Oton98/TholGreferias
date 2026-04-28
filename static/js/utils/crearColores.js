export function crearColores(type, listaColores) {

    const container = document.getElementById("colorsContainer");

    // Crear sección
    const section = document.createElement("div");
    section.classList.add("special-colors-container-div");

    // Título (Clásicos / Especiales)
    const title = document.createElement("h3");
    title.textContent = type;
    title.classList.add("special-colors-div-title");

    section.appendChild(title);

    // Contenedor de cards
    const grid = document.createElement("div");
    grid.classList.add("special-colors-div-grid");

    // Loop de colores
    listaColores.forEach(color => {

        const card = document.createElement("div");
        card.classList.add("special-colors-div-grid-card");

        const img = document.createElement("img");
        img.src = color.img;
        img.alt = color.nombre;

        const name = document.createElement("p");
        name.textContent = color.nombre;

        card.appendChild(img);
        card.appendChild(name);

        grid.appendChild(card);
    });

    section.appendChild(grid);
    container.appendChild(section);
}