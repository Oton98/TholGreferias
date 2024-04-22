// const apiIp = "www.thol.com.ar";
const apiIp = "192.168.100.3";

const loginbtn = document.getElementById('loginbtn');
loginbtn.addEventListener('click', checkIdentidad);

async function checkIdentidad(e) {
    e.preventDefault();
    const usuario = document.getElementById("userName").value;
    const pwd = document.getElementById("userPassword").value;

    const response = await fetch(`http://${apiIp}/admin/login`, {
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