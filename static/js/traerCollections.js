export async function traerColleciones() {
    try {
        const response = await fetch('http://127.0.0.1:5000/getAllCollection');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

