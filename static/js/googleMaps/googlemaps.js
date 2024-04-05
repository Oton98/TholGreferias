import { traerDistributors } from "../traerDistributors.js";
import { imagenMarker } from "../utils/constantes.js";

(g => { var h, a, k, p = "The Google Maps JavaScript API", c = "google", l = "importLibrary", q = "__ib__", m = document, b = window; b = b[c] || (b[c] = {}); var d = b.maps || (b.maps = {}), r = new Set, e = new URLSearchParams, u = () => h || (h = new Promise(async (f, n) => { await (a = m.createElement("script")); e.set("libraries", [...r] + ""); for (k in g) e.set(k.replace(/[A-Z]/g, t => "_" + t[0].toLowerCase()), g[k]); e.set("callback", c + ".maps." + q); a.src = `https://maps.${c}apis.com/maps/api/js?` + e; d[q] = f; a.onerror = () => h = n(Error(p + " could not load.")); a.nonce = m.querySelector("script[nonce]")?.nonce || ""; m.head.append(a) })); d[l] ? console.warn(p + " only loads once. Ignoring:", g) : d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n)) })({
    key: "AIzaSyAw5nx-T06If4bIODIynyDosQhMrf5eAQA",
    // Add other bootstrap parameters as needed, using camel case.
    // Use the 'v' parameter to indicate the version to load (alpha, beta, weekly, etc.)
});

// Initialize and add the map
export let map;

export async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    const { Marker } = await google.maps.importLibrary("marker");
    const distribuidores = await traerDistributors();
    // The location of CABA
    const position = { lat: -34.6158238, lng: -58.4332985 };

    // The map, centered at CABA
    map = new Map(document.getElementById("map-container"), {
        zoom: 11.5,
        center: position,
        mapId: "59cd492fb79389df",
    });

    distribuidores.forEach(distribuidor => {
        const lat = parseFloat(distribuidor.latitud);
        const lng = parseFloat(distribuidor.longitud);
    
        if (!isNaN(lat) && !isNaN(lng)) {
            const marker = new Marker({
                map: map,
                position: { lat: lat, lng: lng },
                title: distribuidor.nombre,
                icon: {
                    url: imagenMarker,
                    scaledSize: new google.maps.Size(40, 60)
                }
            });
        } else {
            console.error('Latitud o longitud inválida:', distribuidor);
        }
    });

}
