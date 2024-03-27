let searcher = document.getElementById('searcher');
let animacionBuscando;

searcher.addEventListener('keyup', async (event) => {
    let listaResultados = document.getElementById('results');
    let palabra = event.target.value.trim();

    if (palabra.length >= 3) {
        try {
            if (!animacionBuscando) {
                animacionBuscando = document.createElement('i');
                animacionBuscando.classList = "fa-solid fa-arrows-spin navbar-items-item-searcher-list-itemcargando";
                listaResultados.appendChild(animacionBuscando);
            }

            const response = await fetch(`http://127.0.0.1:5000/searchword/${palabra}`);

            if (animacionBuscando && listaResultados.contains(animacionBuscando)) {
                listaResultados.removeChild(animacionBuscando);
            }

            if (!response.ok) {
                throw new Error('Error de red al obtener datos');
            }

            const resultados = await response.json();

            const mockResultados = [
                { nombre: 'Producto 1', tipo: 'Tipo A' },
                { nombre: 'Producto 2', tipo: 'Tipo B' },
                // { nombre: 'Producto 3', tipo: 'Tipo C' },
                // { nombre: 'Producto 4', tipo: 'Tipo D' }
            ];

            // Limpiar resultados anteriores
            listaResultados.innerHTML = '';

            if (mockResultados.length > 0) {
                mockResultados.forEach(resultado => {
                    let contenedor = document.createElement('div');
                    contenedor.classList = "navbar-items-item-searcher-list-item";
                    contenedor.innerText = `${resultado.nombre} - ${resultado.tipo}`;
                    listaResultados.appendChild(contenedor);
                });

            } else {
                let contenedorErroneo = document.createElement('div');
                contenedorErroneo.classList = "navbar-items-item-searcher-list-item";
                contenedorErroneo.innerText = 'No se encontró resultados';
                listaResultados.appendChild(contenedorErroneo);
            }

        } catch (error) {
            if (animacionBuscando && listaResultados.contains(animacionBuscando)) {
                listaResultados.removeChild(animacionBuscando);
            }
            console.error('Error:', error.message);
        }
    } else {
        listaResultados.style.display = 'none'; // Ocultar la lista si la palabra es corta
    }
});