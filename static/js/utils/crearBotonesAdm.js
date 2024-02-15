export function crearBotonActualizar(id) {
    const button = document.createElement('button');
    button.textContent = 'Actualizar';
    button.addEventListener('click', () => {
        window.location.href = `/redirectProduct/${id}`;
    });
    return button;
}

export function crearBotonBorrar(id) {
    const button = document.createElement('button');
    button.textContent = 'Borrar';
    button.addEventListener('click', () => {
        if (confirm('¿Estás seguro de que deseas borrar este producto?')) {
            // Enviar solicitud de borrado al backend
            fetch(`/product/${id}`, {
                method: 'DELETE',
            })
            .then(response => {
                if (response.ok) {
                    alert('Producto borrado exitosamente');
                    window.location.reload(); // Recargar la página después de borrar
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
