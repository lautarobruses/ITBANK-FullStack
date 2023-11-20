const passwordInput = document.getElementById("id_password");
const toggleButton1 = document.getElementById("toggle-password-1");
const showIcon = document.getElementsByClassName("show-icon");
const hideIcon = document.getElementsByClassName("hide-icon");

const confirmPasswordInput = document.getElementById("id_confirm_password");
const toggleButton2 = document.getElementById("toggle-password-2");

toggleButton1.addEventListener('click', () => {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showIcon[0].style.display = "none";
        hideIcon[0].style.display = "block";
    } else {
        passwordInput.type = "password";
        showIcon[0].style.display = "block";
        hideIcon[0].style.display = "none";
    }
});

toggleButton2.addEventListener('click', () => {
    if (confirmPasswordInput.type === "password") {
        confirmPasswordInput.type = "text";
        showIcon[1].style.display = "none";
        hideIcon[1].style.display = "block";
    } else {
        confirmPasswordInput.type = "password";
        showIcon[1].style.display = "block";
        hideIcon[1].style.display = "none";
    }
});