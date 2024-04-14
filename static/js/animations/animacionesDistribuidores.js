export function animacionDistribuidores(regiones, regionContainers) {
    // Asignar animación a todos
    regiones.forEach(region => {
        const icono = region.querySelector('.fa-chevron-down');

        icono.addEventListener('click', (event) => {
            event.stopPropagation(); // Evitar que el clic se propague a los elementos hijos

            // Cerrar todos los menús de compañías excepto el de la región clickeada
            regiones.forEach(r => {
                if (r !== region) {
                    r.classList.remove('show');
                    const iconoCerrar = r.querySelector('.fa-chevron-down');
                    iconoCerrar.classList.remove('rotated-icon');
                }
            });

            // Toggle la clase show para mostrar u ocultar el menú de compañías
            region.classList.toggle('show');
            icono.classList.toggle('rotated-icon');
        });
    });

    // Mostrar Ciudad Autónoma de Buenos Aires al cargar la página
    regionContainers.forEach(regionContainer => {
        if (regionContainer.innerText.trim() === "Ciudad Autónoma de Buenos Aires") {
            const region = regionContainer.closest('.partnership-locations-regions');

            region.classList.add('show');

            const icono = region.querySelector('.fa-chevron-down');
            icono.classList.add('rotated-icon');
        }
    });
}