export function crearBotonActualizar(id) {
    const button = document.createElement('button');
    button.textContent = 'Actualizar';
    button.addEventListener('click', () => {
        window.location.href = `/redirectProduct/${id}`;
    });
    return button;
}

export function crearBotonBorrar(id, ruta) {
    const button = document.createElement('button');
    
    button.textContent = 'Borrar';
    button.addEventListener('click', () => {
        if (confirm('¿Estás seguro de que deseas borrar este producto?')) {
           console.log(id)
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
