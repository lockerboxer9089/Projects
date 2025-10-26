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

function submit() {
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var email = document.getElementById("email").value;
    var rating = document.querySelector('input[name="rating"]:checked')?.value || 'Not Provided';

    var improvements = [];
    if (document.getElementById("option1").checked) {
        improvements.push(document.getElementById("option1").value);
    }
    if (document.getElementById("option2").checked) {
        improvements.push(document.getElementById("option2").value);
    }
    if (document.getElementById("option3").checked) {
        improvements.push(document.getElementById("option3").value);
    }

    sessionStorage.setItem('reviewData', JSON.stringify({
        firstName: fname,
        lastName: lname,
        email: email,
        rating: rating,
        improvements: improvements
    }));

    location.replace("final.html");
}