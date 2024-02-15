export async function traerAccesorios() {
    try {
        const response = await fetch('http://127.0.0.1:5000/getAllAccesories');
        
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

export async function traerColleciones() {
    try {
        const response = await fetch('http://127.0.0.1:5000/getAllCollection');
        
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
        const response = await fetch('http://127.0.0.1:5000/getAllfaucets');
        
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
        const response = await fetch('http://127.0.0.1:5000/getAlladdons');
        
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
        const response = await fetch(`http://127.0.0.1:5000/getProduct/${id}`)

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
        const response = await fetch(`http://127.0.0.1:5000/getCollection/${id}`)

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

