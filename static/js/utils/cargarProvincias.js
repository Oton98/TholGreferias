import { provinciasCoordenadas } from "./constantes.js";

document.addEventListener("DOMContentLoaded", function() {
    cargarProvincias();
});

export function cargarProvincias(){
    provinciasCoordenadas.forEach(provincia => {
        let select = document.getElementById("ProvinciaAdress");
        let option = document.createElement("option");
        option.innerText = provincia.nombre;
        option.value = provincia.nombre; 
        select.appendChild(option);
    });
}

