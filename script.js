const toggleBtn = document.getElementById("toggle-mode");
const icon = document.getElementById("mode-icon");

toggleBtn.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        icon.classList.remove("bi-moon-stars-fill");
        icon.classList.add("bi-sun-fill");
    } else {
        icon.classList.remove("bi-sun-fill");
        icon.classList.add("bi-moon-stars-fill");
    }
});
