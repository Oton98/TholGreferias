export function mezclarArray(array, productoId) {
    const filtrado = array.filter(producto => producto.id !== productoId);
    for (let i = filtrado.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}