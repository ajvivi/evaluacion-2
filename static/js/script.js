document.addEventListener("DOMContentLoaded", () => {
    const rutaActual = window.location.pathname;
    const enlaces = document.querySelectorAll("#menuPrincipal .nav-link");

    enlaces.forEach((enlace) => {
        const rutaEnlace = new URL(enlace.href).pathname;
        const esPaginaActual = rutaEnlace === rutaActual;

        enlace.classList.toggle("active", esPaginaActual);

        if (esPaginaActual) {
            enlace.setAttribute("aria-current", "page");
        } else {
            enlace.removeAttribute("aria-current");
        }
    });
});