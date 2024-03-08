import { crearBotonActualizar, crearBotonBorrar } from "./crearBotonesAdm.js";

export function crearTableData(valor, fila) {
    let td = document.createElement("td");
    let p = document.createElement("p");
    p.innerText = valor
    p.classList = "table-tbody-tr-td-p";
    td.appendChild(p);
    td.classList = "table-tbody-tr-td";
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

export function crearPDFVisual(valor, fila){
    let td = document.createElement("td");
    td.classList = "table-tbody-tr-td";
    let pdf = document.createElement('a');
    let iconPdf = document.createElement('i');
    iconPdf.classList = "fa-regular fa-file-pdf";
    iconPdf.style = "color: #D9D9D9; font-size: 32px;"
    pdf.href= valor;
    pdf.appendChild(iconPdf);
    td.appendChild(pdf)
    fila.appendChild(td);
    
}

export function crearTDimagen(valor, fila) {
    let td = document.createElement("td");
    td.classList = "table-tbody-tr-td";
    let imagen = document.createElement('img');
    imagen.src = valor;
    imagen.classList="table-tbody-tr-td-img"
    td.appendChild(imagen)
    fila.appendChild(td);
}

export function crearCeldaBotones(id, ruta) {
    const celda = document.createElement("td");
    celda.classList = "table-tbody-tr-td"

    // Crear y agregar botones
    const botonBorrar = crearBotonBorrar(id, ruta);
    const botonActualizar = crearBotonActualizar(id, ruta);

    celda.appendChild(botonActualizar);
    celda.appendChild(botonBorrar);

    return celda;
}