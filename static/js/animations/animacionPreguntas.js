document.addEventListener('DOMContentLoaded', function() {
    let preguntas = document.querySelectorAll('.consultation-menu-matters-matter-question');

    preguntas.forEach((pregunta, index) => {
        pregunta.addEventListener('click', function() {
            // Obtén la respuesta correspondiente a la pregunta
            let respuesta = document.getElementById(`answer${index + 1}`);
            
            if (respuesta.classList.contains("mostrar-respuesta")) {
                // Si la respuesta está abierta, ciérrala
                respuesta.classList.remove("mostrar-respuesta");
            } else {
                // Si la respuesta está cerrada, cierra todas y ábrela
                cerrarRespuestas();
                respuesta.classList.add("mostrar-respuesta");
            }
        });
    });
});

function cerrarRespuestas() {
    let respuestasActivas = document.querySelectorAll('.consultation-menu-matters-matter-answer.mostrar-respuesta');
    respuestasActivas.forEach(respuesta => {
        respuesta.classList.remove("mostrar-respuesta");
    });
}