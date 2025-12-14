const cleanValue = str => str.split(/\r?\n/).map(line => line.trim()).filter(line => line).join("\n");

const initialMealTimes = cleanValue(document.getElementById("meal_time").value);

const logout = () => window.location.href = "/logout";

function togglePassword() {
    const passwordField = document.getElementById("password");
    const eyeIcon = document.querySelector(".toggle-password");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        eyeIcon.textContent = "Ocultar Contraseña";
    } else {
        passwordField.type = "password";
        eyeIcon.textContent = "Mostrar Contraseña";
    }
}

document.getElementById("meal-dashboard-form").addEventListener("submit", function(event) {
    const textarea = document.getElementById("meal_time");
    const passwordField = document.getElementById("password");

    if (cleanValue(textarea.value) === initialMealTimes) {
        textarea.removeAttribute("name");
    }

    if (passwordField.value.trim() === "") {
        passwordField.removeAttribute("name");
    }
});
