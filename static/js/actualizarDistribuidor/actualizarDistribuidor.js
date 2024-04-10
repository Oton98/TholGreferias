import { getIdFromURL } from "../utils/capturarIdUrl.js";
import { cargarProvincias } from "../utils/cargarProvincias.js";
import { cargarDatosDistribuidor } from "./cargarDatosDistribuidor.js";
import { enviarInformacion } from "./enviarInformacion.js";

document.addEventListener("DOMContentLoaded", async function () {
    const distribuidorId = getIdFromURL();
    cargarProvincias();
    try {
        await cargarDatosDistribuidor(distribuidorId);
    } catch (error) {
        console.error('Error al cargar datos del distribuidor:', error);
    }

    const btnActualizar = document.getElementById('updateDistributor');

    if (btnActualizar) {
        btnActualizar.addEventListener('click', async function (event) {
            event.preventDefault(); // Evitar el comportamiento predeterminado del botón

            try {
                await enviarInformacion(distribuidorId);
            } catch (error) {
                console.error('Error al enviar la información:', error);
            }
        });
    } else {
        console.error('No se encontró el botón "Actualizar"');
    }
});

