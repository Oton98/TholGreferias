const iconOpen = document.getElementById('icon-open');
const iconClose = document.getElementById('icon-close');
const navbarLinks = document.querySelector('.navbar-items');
const navbar = document.getElementById('navbar');

let isIconOpenVisible = true;

function checkSize() {
    var width = window.innerWidth;

    if (width > 810 && isIconOpenVisible) {
        navbarLinks.classList.remove('activado');
        iconOpen.style.display = 'none';
        iconClose.style.display = 'none';
        navbar.style.height = 'auto';
    } else {
        iconOpen.style.display = 'block';
        iconClose.style.display = 'none';
        navbar.style.height = 'auto';
    }
}

window.addEventListener('resize', checkSize);

iconOpen.addEventListener('click', function () {
  navbarLinks.classList.add('activado');
  iconOpen.style.display = 'none';
  iconClose.style.display = 'block';
//   navbar.style.height = '100vh';
  isIconOpenVisible = false;
});

iconClose.addEventListener('click', function () {
  navbarLinks.classList.remove('activado');
  iconOpen.style.display = 'block';
  iconClose.style.display = 'none';
//   navbar.style.height = 'auto';
  isIconOpenVisible = true;
});

// // Llamada inicial para configurar el estado inicial
checkSize();
