import { map } from "./googlemaps.js";

export function crearBotonesProvincia(provincias, distribuidores) {

    let container = document.getElementById("locationsContainer");

    provincias.forEach(provincia => {
        let region = document.createElement("div");
        let regionContainerTitulo = document.createElement("div");
        let regionTitulo = document.createElement("h3");
        let icono = document.createElement("i");

        //Creo el titulo de la seccion
        region.classList = "partnership-locations-regions";
        regionContainerTitulo.classList = "partnership-locations-regions-cityTitle";
        regionTitulo.innerText = provincia;
        icono.classList = "fa-solid fa-chevron-down";

        regionContainerTitulo.appendChild(regionTitulo);
        regionContainerTitulo.appendChild(icono);

        let companiasContainer = document.createElement("div");
        companiasContainer.classList = "partnership-locations-regions-companys";

        //Filtrado de distribuidores por provincia y creacion de tarjeta interna
        const distribuidoresFiltrados = distribuidores.filter(distribuidor => distribuidor.Localidad === provincia);
        
        distribuidoresFiltrados.forEach(empresa => {
            let contenedorEmpresa = document.createElement("div");
            let tituloEmpresa = document.createElement("h3");

            contenedorEmpresa.classList = "partnership-locations-regions-companys-company";
            tituloEmpresa.innerText = empresa.nombre;
            contenedorEmpresa.appendChild(tituloEmpresa);

            for (let campo in empresa) {
                if (campo !== "Localidad" && campo !== "id" && campo !== "nombre" && campo !== "longitud" && campo !== "latitud" && empresa[campo]) {
                    let campoCapitalizado = campo.charAt(0).toUpperCase() + campo.slice(1);
                    let etiquetaCampo = document.createElement("p");
                    etiquetaCampo.innerText = `${campoCapitalizado}: ${empresa[campo]}`;
                    contenedorEmpresa.appendChild(etiquetaCampo);
                }
            }

            contenedorEmpresa.addEventListener("click", () => {
                map.setCenter({ lat: parseFloat(empresa.latitud), lng: parseFloat(empresa.longitud) });
                map.setZoom(17);
            });

            companiasContainer.appendChild(contenedorEmpresa);

        })

        region.appendChild(regionContainerTitulo);
        region.appendChild(companiasContainer);
        container.appendChild(region);
    });
}