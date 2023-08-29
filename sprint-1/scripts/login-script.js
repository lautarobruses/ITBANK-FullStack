var arrayUser = JSON.parse(localStorage.getItem("arrayUser"));
if (arrayUser == undefined) {
    arrayUser = [];
}

var user = {
    username: String,
    nameUser: String,
    lastNameUser: String,
    paswordUser: String,
    emailUser: String,
    phoneUser: Number,
    nationUser: String,
    dniUser: Number,
};

function sendRegisterForm() {
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden");
    }
    else {
        let name = document.getElementById('name').value;
        let lastName = document.getElementById('last-name').value;
        let email = document.getElementById('email').value;
        let nationality = document.getElementById('select-nationality').value;
        let phone = document.getElementById('phone').value;
        let dni = document.getElementById('dni').value;

        let username = name + lastName;
        username = username.toLowerCase();

        user = { username, name, lastName, password, email, nationality, phone, dni };

        arrayUser.push(user);

        localStorage.setItem("arrayUser", JSON.stringify(arrayUser));
        
        alert("Te haz registrado correctamente");

        let form = document.getElementById("register-form");
        form.action = "login.html";
    }

}

function checkUser() {
    let userTag = document.getElementById('user-tag').value;
    let password = document.getElementById('password').value;

    let i = 0;
    let userLoad = arrayUser[0];
 
    while (i+1 < arrayUser.length && (userLoad.username != userTag || userLoad.email != userTag && userLoad.password != password)) {
        console.log(userLoad.username != userTag);
        i = i + 1;

        userLoad = arrayUser[i];
    }
    if (i+1 >= arrayUser.length) {
        console.log("adios");
        alert("usuario incorrecto");
    }
    else {
        let form = document.getElementById("login-form");
        form.action = "../index.html";
    }
}



function showPassword(inputID, iconID) {
    let password = document.getElementById(inputID);
    let icon = document.getElementById(iconID);

    if (password.type === 'password') {
        password.type = 'text';
        icon.src = "/resources/img/icons/ojo.svg";
    } else {
        password.type = 'password';
        icon.src = "/resources/img/icons/ojo-tachado.svg";
    }
}

function checkPassword() {
    let password = document.getElementById('password').value;

    console.log(password);
}

function confirmPassword() {

}