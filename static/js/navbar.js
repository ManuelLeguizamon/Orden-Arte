document.addEventListener("DOMContentLoaded", () => {
    const hamburguesa = document.getElementById("hamburguesa");
    const ulBar = document.getElementById("ul-bar");
    const cerrarMenu = document.getElementById("cerrar-menu");

    if (hamburguesa && ulBar) {
        hamburguesa.addEventListener("click", () => {
            ulBar.classList.add("active");
        });
    }

    if (cerrarMenu && ulBar) {
        cerrarMenu.addEventListener("click", (e) => {
            e.stopPropagation();   // 👈 clave
            ulBar.classList.remove("active");
        });

    }
});
