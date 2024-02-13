import { traerColleciones } from "./traerCollections.js";
import {selectCollections} from "./utils/constantes.js";

window.addEventListener('DOMContentLoaded', async (event) => {
    try {
        const dataCollections = await traerColleciones();
        for (var key in dataCollections) 
        if (dataCollections.hasOwnProperty(key)) {
            const collection = dataCollections[key];
            const option = document.createElement("option");
            option.value = collection.nombre;
            option.text = collection.nombre;
            selectCollections.add(option)
        }
    } catch (error) {
        console.error('Error:', error);
    }
});


