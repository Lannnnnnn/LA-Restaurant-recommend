/* On search, scroll down to results */
function scrolldown() {
    var first_result = document.getElementById("result_element");
    first_result.scrollIntoView();
}

/* When results are produced, fade them in */
function fade_in(element) {
    var opacity = 0.01;
    var timer = setInterval(function () {
        if (opacity >= 1){
            clearInterval(timer);
        }
        element.style.opacity = opacity;
        element.style.filter = opacity*100;
        opacity += opacity * 0.1;
    }, 25);
}

/* Allows the food and restaurant buttons to be toggled,
   where only one button can be active at a time */
function toggle(button) {
    var foodbutton = document.getElementById("foodButton");
    var restbutton = document.getElementById("restaurantButton");
    var veganbutton = document.getElementById("veganButton");
    var foodCheck = document.getElementById("foodButtonCheck");
    var restCheck = document.getElementById("restButtonCheck");
    if (button == veganbutton && button.value == "OFF") {
        button.value = "ON"
        button.style = "background-color: green; color: white"
    } else if (button == veganbutton && button.value == "ON") {
        button.value = "OFF"
        button.style = "background-color: lightgray; color: black"
    }
    if (button == restbutton && button.value == "OFF") {
        button.value = "ON";
        restCheck.checked = true;
        button.style = "background-color: #d32323; color: white";
        foodbutton.value = "OFF";
        foodCheck.checked = false;
        foodbutton.style = "background-color: lightgray; color: black";
    } else if (button == foodbutton && button.value == "OFF") {
        button.value = "ON";
        foodCheck.checked = true;
        button.style = "background-color: #d32323; color: white";
        restbutton.value = "OFF";
        restCheck.checked = false;
        restbutton.style = "background-color: lightgray; color: black";
    };
}