async function crearProducto(productName, isAvailable, isFeaturedItem){
    console.log("enviado")
    const response = await fetch('http://127.0.0.1:5000/products', {
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




