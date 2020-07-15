function foodFunction() {
    var foodOutput;
    var food = document.getElementById("food-input").value;
    var foodString = " is a delicious food! Nice choice!";
    var foodStringTwo = " are a delicious food! Great choice!";
    switch(food) {
        case "Nachos":
            foodOutput = "Nachos" + foodStringTwo;
        break;
        case "Tacos":
            foodOutput = "Tacos" + foodStringTwo;
        break;
        case "Pizza":
            foodOutput = "Pizza" + foodString;
        break;
        case "Sushi":
            foodOutput = "Sushi" + foodString;
        break;
        default:
            foodOutput = "Please choose a food from the list above.";
    }
    document.getElementById("output").innerHTML = foodOutput;
}

function myFunction() {
    var change = document.getElementsByClassName("change");
    change[0].innerHTML = "Which food tastes the best?";
}

function canvasFunction() {
    var can = document.getElementById("canvas-id");
    var vas = can.getContext("2d");
    vas.moveTo(0,70);
    vas.lineTo(250, 70);
    vas.lineTo(0, 100);
    vas.lineTo(250, 100);
    vas.lineTo(0, 70);
    vas.stroke();
}

function addBackground() {
    var can = document.getElementById("canvas-id");
    var vas = can.getContext("2d");
    var bg = vas.createLinearGradient(0, 0, 150, 0)
    bg.addColorStop(0, "white");
    bg.addColorStop(1, "lightgrey");
    vas.fillStyle = bg;
    vas.fillRect(0,0,250,250);
}

addBackground();