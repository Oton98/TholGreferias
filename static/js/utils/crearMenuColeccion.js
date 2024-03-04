import { imagenMonomando, imagenBimando, imagenFreestanding, imagenAccesorios, imagenComplementos } from "./constantes.js";
import { crearTarjetaTipo } from "./crearTarjetaTipo.js";

export function crearTarjetaMenuColecciones(tipo, containerTarjetas, coleccionNombre) {
    let link = `/nuestrodisenio/coleccion/${coleccionNombre}/productmenu/${tipo}`;
    
    switch (tipo) {
        case "Grifería monocomando":
            const tarjetaMonocomando = crearTarjetaTipo(imagenMonomando, link);
            containerTarjetas.appendChild(tarjetaMonocomando);
            break;
        case "Grifería Bimando":
            const tarjetaBimando = crearTarjetaTipo(imagenBimando, link);
            containerTarjetas.appendChild(tarjetaBimando);
            break;
        case "Grifería Freestanding":
            const tarjetaFreestanding = crearTarjetaTipo(imagenFreestanding, link);
            containerTarjetas.appendChild(tarjetaFreestanding);
            break;
        case "Accesorio":
            const tarjetaAccesorio = crearTarjetaTipo(imagenAccesorios, link);
            containerTarjetas.appendChild(tarjetaAccesorio);
            break;
        case "Complemento":
            const tarjetaComplemento = crearTarjetaTipo(imagenComplementos, link);
            containerTarjetas.appendChild(tarjetaComplemento);
            break;
    }
}



