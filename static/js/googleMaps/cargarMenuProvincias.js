import { map } from "./googlemaps.js";

export function crearBotonesProvincia(provincias, distribuidores) {

    let container = document.getElementById("locationsContainer");

    provincias.forEach(provincia => {
        let region = document.createElement("div");
        let regionContainerTitulo = document.createElement("div");
        let regionTitulo = document.createElement("h3");

        //Creo el titulo de la seccion
        region.classList = "partnership-locations-regions";
        regionContainerTitulo.classList = "partnership-locations-regions-cityTitle";
        regionTitulo.innerText = provincia;

        regionContainerTitulo.appendChild(regionTitulo);

        let companiasContainer = document.createElement("div");
        companiasContainer.classList = "partnership-locations-regions-companys";

        //Filtrado de distribuidores por provincia y creacion de tarjeta interna
        const distribuidoresFiltrados = distribuidores.filter(distribuidor => distribuidor.provincia === provincia);
        
        distribuidoresFiltrados.forEach(empresa => {
            let contenedorEmpresa = document.createElement("div");
            let tituloEmpresa = document.createElement("h3");
            let direccionFisica = document.createElement("p");

            contenedorEmpresa.classList = "partnership-locations-regions-companys-company";
            tituloEmpresa.innerText = empresa.nombre;
            direccionFisica.innerText = empresa.direccion;

            contenedorEmpresa.addEventListener("click", () => {
                map.setCenter({ lat: parseFloat(empresa.latitud), lng: parseFloat(empresa.longitud) });
                map.setZoom(17);
            });

            contenedorEmpresa.appendChild(tituloEmpresa);
            contenedorEmpresa.appendChild(direccionFisica);

            companiasContainer.appendChild(contenedorEmpresa);

        })

        region.appendChild(regionContainerTitulo);
        region.appendChild(companiasContainer);
        container.appendChild(region);
    });
}