// const apiIp = "www.thol.com.ar";
const apiIp = "192.168.100.3";

export async function traerAccesorios() {
    try {
        const response = await fetch(`http://${apiIp}/productos/getAllAccesories`);
        
        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerGriferias() {
    try {
        const response = await fetch(`http://${apiIp}/productos/getAllfaucets`);
        
        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerComplementos() {
    try {
        const response = await fetch(`http://${apiIp}/productos/getAlladdons`);
        
        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerProducto(id){
    try{
        const response = await fetch(`http://${apiIp}/productos/getProduct/${id}`)

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
    
}

export async function traerTipoProducto(id){
    try {
        const response = await fetch(`http://${apiIp}/productos/getproductsbycollection/${id}`);

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerProdctoxTipo(id, tipo){
    try {
        const response = await fetch(`http://${apiIp}/productos/getproductsbytypebycollection/${id}/${tipo}`);

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerProductoxColeccion(id){
    try {
        const response = await fetch(`http://${apiIp}/productos/getproductsbycollection/${id}`);

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

export async function traerProductoDestacados(){
    try {
        const response = await fetch(`http://${apiIp}/productos/getallfeatureproducts`);

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        console.error('Error:', error.message);
        throw error;
    }
}

