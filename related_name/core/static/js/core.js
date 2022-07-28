const btn = document.getElementById("delete-btn")
if (!null) {
    btn.addEventListener('click', (event) => {
        const element = document.querySelector(".message");
        element.style.width = "0px";
    });

}