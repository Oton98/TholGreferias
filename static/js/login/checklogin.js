const loginbtn = document.getElementById('loginbtn');
loginbtn.addEventListener('click', checkIdentidad);

async function checkIdentidad() {
    const usuario = document.getElementById("userName").value;
    const pwd = document.getElementById("userPassword").value;

    const response = await fetch('http://127.0.0.1:5000/admin/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            userName: usuario,
            userPassword: pwd,
        })
    });

    const data = await response.json();

    if (data.redirect) {
        window.location.href = data.redirect;
    }

}