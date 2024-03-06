import { crearBotonesIndex } from "../utils/crearBotonesIndex.js";
import { tarjetaProductosRelacionados } from "../cards/crearProductosRelacionados.js"


export function cargarPantallaProducto(productosDeLaColeccion, producto, containerTarjeta) {

    let tarjetaImgDiv = document.createElement('div');
    tarjetaImgDiv.classList = "product-container-card-sectionImage";
 
    let tarjetaImg = document.createElement('img');
    tarjetaImg.classList = "product-container-card-sectionImage-img";
    tarjetaImg.src = producto.imagen;

    tarjetaImgDiv.appendChild(tarjetaImg);

    let tarjetaTextDiv = document.createElement('div')
    tarjetaTextDiv.classList = "product-container-card-sectionText";

    let productheader = document.createElement('div');
    productheader.classList = "product-container-card-sectionText-header";

    let productTitle = document.createElement('h3');
    productTitle.classList = "product-container-card-sectionText-header-title";
    productTitle.innerText = producto.tipo //aca el titulo

    productheader.appendChild(productTitle);
    
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

    let textContainer = document.createElement('div');
    textContainer.classList = "product-container-card-sectionText-description";
    let text = document.createElement('p');
    text.innerText = producto.descripcion;

    textContainer.appendChild(text);

    let buttonContainer = document.createElement('div');
    buttonContainer.classList = "product-container-card-sectionText-buttons";
    let buttonMedidas = crearBotonesIndex("Descargar medidas", "button-primary", producto.medidas)
    let buttonManual = crearBotonesIndex("Descagar manual", "button-secondary", producto.manual);
    buttonContainer.appendChild(buttonMedidas);
    buttonContainer.appendChild(buttonManual);

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