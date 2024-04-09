// const apiIp = "200.58.107.86";
const apiIp = "192.168.100.3";


export async function traerColleciones() {
    try {
        const response = await fetch(`http://${apiIp}/colecciones/getAllCollection`);
        
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

export async function traerColeccion(id){
    try{
        const response = await fetch(`http://${apiIp}/colecciones/getCollection/${id}`)

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

