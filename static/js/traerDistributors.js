const apiIp = "www.thol.com.ar";
// const apiIp = "192.168.100.3";


export async function traerDistributors() {
    try {
        const response = await fetch(`https://${apiIp}/distribuidores/getalldistributors`);

        if (!response.ok) {
            throw new Error('Error de red al obtener datos');
        }

        const data = await response.json();

        return data;

    } catch (error) {
        console.error('Error:', error.message);
        setTimeout(() => {
            window.location.reload();
        }, 2000);
        throw error;

    }
}

export async function traerDistributor(id) {
    try {
        const response = await fetch(`https://${apiIp}/distribuidores/getdistributor/${id}`);

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

