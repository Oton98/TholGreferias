import { traerProducto } from "../traerProducts.js";
import { traerColeccion } from "../traerCollections.js";
import { cargarColecciones } from "../index/cargarColecciones.js";
import { getIdFromURL } from "./capturarIdUrl.js";

// Función para configurar el action del formulario con el id
async function setFormAction() {
    try {

        cargarColecciones();

        const form = document.querySelector('.control-panelbox-form form');
        const productId = getIdFromURL();
        form.id = productId;

        const product = await traerProducto(productId);
        const collection = await traerColeccion(product.coleccion_id);

        if (productId) {
            form.id = productId;
            document.getElementById('productName').value = product.nombre
            document.getElementById('productCode').value = product.codigo
            document.getElementById('productType').value = product.tipo
            document.getElementById('collection').value = collection.nombre
            document.getElementById('descriptionProduct').value = product.descripcion
            document.getElementById('productImage').value = product.imagen
            document.getElementById('productColores').value = product.colores
            document.getElementById('collectionManualDetails').value = product.manual
            document.getElementById('collectionManualInstalation').value = product.medidas
            document.getElementById('isFeaturedProducto').checked = product.esDestacado
            document.getElementById('isAvailable').checked = product.estaDisponible


        } else {
            console.error('No se encontró el id del producto en la URL.');
        }
    } catch (error) {
        console.error('Error al obtener el producto:', error);
    }
}

// Ejecutar la función al cargar la página
document.addEventListener('DOMContentLoaded', setFormAction);