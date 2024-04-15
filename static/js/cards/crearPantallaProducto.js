import { crearBotonesIndex } from "../utils/crearBotonesIndex.js";
import { tarjetaProductosRelacionados } from "../cards/crearProductosRelacionados.js"


export function cargarPantallaProducto(productosDeLaColeccion, producto, containerTarjeta) {

    //crea la seccion de la imagen
    let tarjetaImgDiv = document.createElement('div');
    tarjetaImgDiv.classList = "product-container-card-sectionImage";
 
    let tarjetaImg = document.createElement('img');
    tarjetaImg.classList = "product-container-card-sectionImage-img";
    tarjetaImg.src = producto.imagen;

    tarjetaImgDiv.appendChild(tarjetaImg);

    //crea la seccion del texto
    
    let tarjetaTextDiv = document.createElement('div')
    tarjetaTextDiv.classList = "product-container-card-sectionText";

    let productheader = document.createElement('div');

    productheader.classList = "product-container-card-sectionText-header";
    //creo el titulo
    let productTitle = document.createElement('h3');
    productTitle.classList = "product-container-card-sectionText-header-title";
    productTitle.innerText = producto.tipo

    productheader.appendChild(productTitle);
    
    //creo la seccion del codigo y la imagen
    let productId = document.createElement('div');
    productId.classList = "product-container-card-sectionText-id";
    let productIdText = document.createElement('div');
    productIdText.classList = "product-container-card-sectionText-id-text";
    let productName = document.createElement('h4');
    productName.innerText = producto.nombre;
    let productCode = document.createElement('h5');
    productCode.innerText = "CÓDIGO: " + producto.codigo;
    let productImageColors = document.createElement('img');
    productImageColors.classList = "product-container-card-sectionText-id-image";
    productImageColors.src = producto.colores;

    productIdText.appendChild(productName);
    productIdText.appendChild(productCode);

    productId.appendChild(productIdText);
    productId.appendChild(productImageColors);

    //creo la seccion del texto
    let textContainer = document.createElement('div');
    textContainer.classList = "product-container-card-sectionText-description";
    let text = document.createElement('p');
    text.innerText = producto.descripcion;

    textContainer.appendChild(text);

    //creo los botones
    let buttonContainer = document.createElement('div');
    buttonContainer.classList = "product-container-card-sectionText-buttons";
    if (producto.manual) {
        let buttonManual = crearBotonesIndex("Descargar manual", "download", producto.manual);
        buttonContainer.appendChild(buttonManual);
    }

    if (producto.medidas) {
        let buttonMedidas = crearBotonesIndex("Ver medidas", "image", producto.medidas);
        buttonContainer.appendChild(buttonMedidas);
    }

    tarjetaTextDiv.appendChild(productheader);
    tarjetaTextDiv.appendChild(productId);
    tarjetaTextDiv.appendChild(textContainer);
    tarjetaTextDiv.appendChild(buttonContainer);

    containerTarjeta.appendChild(tarjetaImgDiv);
    containerTarjeta.appendChild(tarjetaTextDiv);

    //productos relacionados

    let contenedorProductosRelacionados = document.getElementById('relationedProductContainer');
    tarjetaProductosRelacionados(contenedorProductosRelacionados, productosDeLaColeccion, producto.id);


}