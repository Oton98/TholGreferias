import { provinciasCoordenadas } from "./constantes.js";

document.addEventListener("DOMContentLoaded", function() {
    cargarProvincias();
});

function cargarProvincias(){
    provinciasCoordenadas.forEach(provincia => {
        let select = document.getElementById("DistributorsAdress");
        let option = document.createElement("option");
        option.innerText = provincia.nombre;
        option.value = provincia.nombre; 
        select.appendChild(option);
    });
}

