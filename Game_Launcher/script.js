function redirect(page) {
    if (page == 1) {
        location.replace("redirect_pages/home.html");
    }
    else if (page == 2) {
        location.replace("redirect_pages/login.html");
    }
    else if (page == 3) {
        location.replace("game_pages/hangman.html");
    }
    else if (page == 4) {
        location.replace("game_pages/pong.html");
    }
}

function returnToMain() {
    location.replace("../index.html");
}

function review() {
    location.replace("redirect_pages/review.html");
}

function submitForm(event) {
    event.preventDefault();

    var fName = document.getElementById("fname");
    var lName = document.getElementById("lname");
    let answer = prompt("Do you wish to\n1. Go back to the homepage or \n2. Close this window? Enter the number of your choice");
    if (answer == 1) {
        alert("redirecting to home page!");
        window.location.href = "../index.html";
    }
    else {
        alert("closing window...");
        close();
    }
}