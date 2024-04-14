export function crearBotonActualizar(id, ruta) {
    const button = document.createElement('button');
    button.classList = "button-primary";
    button.textContent = 'Actualizar';
    if (ruta === "productos/deleteProduct") {
        button.addEventListener('click', () => {
            window.location.href = `productos/redirectProduct/${id}`;
        });
    } else if (ruta === "colecciones/deleteCollection"){
        button.addEventListener('click', () => {
            window.location.href = `colecciones/redirectCollection/${id}`;
        });
    } else {
        button.addEventListener('click', () => {
            window.location.href = `distribuidores/redirectdistributors/${id}`;
        });
    }
    return button;
}

    export function crearBotonBorrar(id, ruta) {
        const button = document.createElement('button');
        button.classList = "button-primary";
        button.textContent = 'Borrar';
        button.addEventListener('click', () => {
            if (confirm('¿Estás seguro de que deseas borrar este producto?')) {
                fetch(`/${ruta}/${id}`, {
                    method: 'DELETE',
                })
                    .then(response => {
                        if (response.ok) {
                            alert('Producto borrado exitosamente');
                            window.location.reload();
                        } else {
                            alert('Error al borrar el producto');
                        }
                    })
                    .catch(error => {
                        console.error('Error en la solicitud de borrado:', error);
                    });
            }
        });
        return button;
    }
