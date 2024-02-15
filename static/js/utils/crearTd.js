import { crearBotonActualizar, crearBotonBorrar } from "./crearBotonesAdm.js";

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

export function crearCeldaBotones(id) {
    const celda = document.createElement("td");

    // Crear y agregar botones
    const botonBorrar = crearBotonBorrar(id);
    const botonActualizar = crearBotonActualizar(id);

    celda.appendChild(botonActualizar);
    celda.appendChild(botonBorrar);

    return celda;
}