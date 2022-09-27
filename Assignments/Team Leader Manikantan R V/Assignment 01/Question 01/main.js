// Registration Page
function sendData() {
    var userName = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var phoneNumber = document.getElementById('phoneNumber').value;

    sessionStorage.setItem('USER', userName);
    sessionStorage.setItem('EMAIL', email);
    sessionStorage.setItem('PHONE', phoneNumber);

    return;
}

// Home Page
window.addEventListener('load', ()=> {
    var userName = sessionStorage.getItem('USER');
    var email = sessionStorage.getItem('EMAIL');
    var phoneNumber = sessionStorage.getItem('PHONE');

    document.getElementById('USER').innerHTML = userName;
    // document.getElementById('email').innerHTML = email;
})