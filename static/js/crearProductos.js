// const apiIp = "200.58.107.86";
const apiIp = "192.168.100.3";

async function crearProducto(productName, isAvailable, isFeaturedItem){
    const response = await fetch(`http://${apiIp}/products`, {
    method: 'POST', // Método HTTP
    headers: {
        'Content-Type': 'application/json' // Indica que el cuerpo de la solicitud es un JSON
    },
    body: JSON.stringify({
        // Aquí colocas los datos que deseas enviar en el cuerpo de la solicitud
        product_Name: productName,
        isAvailable: isAvailable,
        isFeaturedProduct: isFeaturedItem
        // ... otros datos del producto
    })
})
}

//esto esta funcionando?


