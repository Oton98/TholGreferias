import { apiIp } from "./utils/constantes.js";


export async function traerDistributors() {
    try {
        const response = await fetch(`http://${apiIp}/distribuidores/getalldistributors`);
        
        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        
        return data;

    } catch (error) {
        console.error('Error:', error.message);
        throw error;
    }
}

