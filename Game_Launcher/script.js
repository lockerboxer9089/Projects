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