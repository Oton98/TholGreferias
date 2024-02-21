export async function traerAccesorios() {
    try {
        const response = await fetch('http://127.0.0.1:5000/productos/getAllAccesories');
        
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

export async function traerGriferias() {
    try {
        const response = await fetch('http://127.0.0.1:5000/productos/getAllfaucets');
        
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

export async function traerComplementos() {
    try {
        const response = await fetch('http://127.0.0.1:5000/productos/getAlladdons');
        
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

export async function traerProducto(id){
    try{
        const response = await fetch(`http://127.0.0.1:5000/productos/getProduct/${id}`)

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


