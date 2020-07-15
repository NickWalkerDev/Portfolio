function checkForm() {
    var X = document.forms["form"]["email"].value;
    var Y = document.forms["form"]["name"].value;
    if (X == "" || Y == "") {
        document.getElementById("incomplete").innerHTML = "FORM INCOMPLETE";
        return false;
    }
    }