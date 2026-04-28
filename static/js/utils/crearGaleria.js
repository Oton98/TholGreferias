export function crearCarousel(listaImagenes) {

    const container = document.querySelector(".special-carousel-section");
    const carouselId = "carouselDinamico";

    // 👉 TITULO (nombre del color)
    const titleDiv = document.createElement("div");
    titleDiv.className = "carousel-title";
    titleDiv.textContent = listaImagenes[0].nombre;

    const carousel = document.createElement("div");
    carousel.id = carouselId;
    carousel.className = "carousel slide";
    carousel.setAttribute("data-bs-ride", "carousel");

    // INDICADORES
    const indicators = document.createElement("div");
    indicators.className = "carousel-indicators";

    // INNER
    const inner = document.createElement("div");
    inner.className = "carousel-inner";

    listaImagenes.forEach((item, index) => {

        // INDICADOR
        const button = document.createElement("button");
        button.type = "button";
        button.setAttribute("data-bs-target", `#${carouselId}`);
        button.setAttribute("data-bs-slide-to", index);
        button.setAttribute("aria-label", `Slide ${index + 1}`);

        if (index === 0) {
            button.classList.add("active");
            button.setAttribute("aria-current", "true");
        }

        indicators.appendChild(button);

        // ITEM
        const itemDiv = document.createElement("div");
        itemDiv.className = "carousel-item";
        itemDiv.setAttribute("data-bs-interval", "4000");

        if (index === 0) {
            itemDiv.classList.add("active");
        }

        // IMAGEN
        const img = document.createElement("img");
        img.src = item.img;
        img.alt = item.nombre;

        // WRAPPER
        const wrapper = document.createElement("div");
        wrapper.className = "img-wrapper";

        wrapper.appendChild(img);
        itemDiv.appendChild(wrapper);

        inner.appendChild(itemDiv);
    });

    // BOTÓN PREV
    const prevBtn = document.createElement("button");
    prevBtn.className = "carousel-control-prev";
    prevBtn.type = "button";
    prevBtn.setAttribute("data-bs-target", `#${carouselId}`);
    prevBtn.setAttribute("data-bs-slide", "prev");

    prevBtn.innerHTML = `
        <span class="custom-control">
            <span class="chevron">&lt;</span>
        </span>
    `;

    // BOTÓN NEXT
    const nextBtn = document.createElement("button");
    nextBtn.className = "carousel-control-next";
    nextBtn.type = "button";
    nextBtn.setAttribute("data-bs-target", `#${carouselId}`);
    nextBtn.setAttribute("data-bs-slide", "next");

    nextBtn.innerHTML = `
        <span class="custom-control">
            <span class="chevron">&gt;</span>
        </span>
    `;

    // ARMADO FINAL
    carousel.appendChild(indicators);
    carousel.appendChild(inner);
    carousel.appendChild(prevBtn);
    carousel.appendChild(nextBtn);

    container.appendChild(carousel);
    container.appendChild(titleDiv); // 👉 agregamos el título

    // 🎬 EVENTO PARA SINCRONIZAR TEXTO
    carousel.addEventListener("slid.bs.carousel", (e) => {
        const index = e.to;

        // fade out
        titleDiv.classList.add("fade-out");

        setTimeout(() => {
            titleDiv.textContent = listaImagenes[index].nombre;

            // fade in
            titleDiv.classList.remove("fade-out");
            titleDiv.classList.add("fade-in");

            setTimeout(() => {
                titleDiv.classList.remove("fade-in");
            }, 300);

        }, 300);
    });
}