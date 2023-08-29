const passwordInput = document.getElementById("password");
const toggleButton = document.getElementById("toggle-password");
const showIcon = document.querySelector(".show-icon");
const hideIcon = document.querySelector(".hide-icon");

toggleButton.addEventListener('click', () => {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showIcon.style.display = "none";
        hideIcon.style.display = "block";
    } else {
        passwordInput.type = "password";
        showIcon.style.display = "block";
        hideIcon.style.display = "none";
    }
});