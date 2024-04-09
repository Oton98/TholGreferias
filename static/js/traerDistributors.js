// const apiIp = "200.58.107.86";
const apiIp = "192.168.100.3";


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

