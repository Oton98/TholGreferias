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
            console.log(resultados);
            // Limpiar resultados anteriores
            listaResultados.innerHTML = '';

            if (resultados.length > 0) {
                resultados.forEach(resultado => {
                    if (resultado.tipo === "Producto") {
                        let contenedor = document.createElement('div');
                        let a = document.createElement('a');
                        a.href = `/nuestrodisenio/coleccion/${resultado.coleccion}/productmenu/${resultado.tipo_producto}/product/${resultado.producto_id}`;
                        a.classList = "navbar-items-item-searcher-list-a";
                        contenedor.classList = "navbar-items-item-searcher-list-a-item"
                        contenedor.innerText = `${resultado.nombre} - ${resultado.tipo_producto} - ${resultado.coleccion}`;
                        a.appendChild(contenedor)
                        listaResultados.appendChild(a);
                    }

                    else {
                        let contenedor = document.createElement('div');
                        let a = document.createElement('a');
                        a.href = `/nuestrodisenio/coleccion-buscada/${resultado.nombre}`;
                        a.classList = "navbar-items-item-searcher-list-a";
                        contenedor.classList = "navbar-items-item-searcher-list-a-item"
                        contenedor.innerText = `${resultado.tipo} - ${resultado.nombre}`;
                        a.appendChild(contenedor)
                        listaResultados.appendChild(a);
                    }
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
        listaResultados.innerHTML = '';
    }
});