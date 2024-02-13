export function crearTableData(valor, fila){
    var td = document.createElement("td");
    td.innerText = valor; 
    fila.appendChild(td);
}

export function crearTableDataProductos(productos, fila) {
    for (const productoInterno of productos) {
        for (const claveInterna of ordenColumnasColeccion) {
            if (claveInterna !== 'id') {
                const valorInterno = productoInterno[claveInterna];
                crearTableData(valorInterno, fila);
            }
        }
    }
}