/* These functions are currently unneeded
function generate_results() {
    document.querySelectorAll('.result_div').forEach(e => e.remove());
    document.querySelectorAll('.result_sep').forEach(e => e.remove());
    fetch('test/testdata/testdata_business.csv').then(response => response.text()).then(data => {
        const lines = data.split(/\r\n|\n/);
        lines.splice(0, 1);
        lines.splice(lines.length-1, 1);
        for (var i in lines) {
            info = lines[i].split(',');
            info[0] = "Name: ".concat(info[0]);
            info[1] = "Address: ".concat(info[1]);
            info[2] = "City: ".concat(info[2]);
            info[3] = "State: ".concat(info[3]);
            info[4] = "Stars: ".concat(info[4]);
            info[5] = "Number of Reviews: ".concat(info[5]);
            info[6] = "Categories: ".concat(info[6]);
            lines[i] = info.join('\n');
        }
        console.log(lines);
        for (var i in lines) {
            var newElement = document.createElement('div');
            var elementSep = document.createElement('br');
            newElement.id = 'result_element';
            newElement.className = 'result_div';
            elementSep.className = 'result_sep';
            newElement.innerHTML = lines[i];
            document.body.appendChild(newElement);
            fade_in(newElement);
            document.body.appendChild(elementSep);
        }
        scrolldown();
    });
}

function scrolldown() {
    var first_result = document.getElementById("result_element");
    first_result.scrollIntoView();
}

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
}*/

function toggle(button) {
    var foodbutton = document.getElementById("foodButton");
    var restbutton = document.getElementById("restaurantButton");
    var foodCheck = document.getElementById("foodButtonCheck");
    var restCheck = document.getElementById("restButtonCheck");
    if (button == restbutton && button.value == "OFF") {
        console.log("restbutton");
        button.value = "ON";
        restCheck.checked = true;
        button.style = "background-color: #d32323; color: white";
        foodbutton.value = "OFF";
        foodCheck.checked = false;
        foodbutton.style = "background-color: lightgray; color: black";
    } else if (button == foodbutton && button.value == "OFF") {
        console.log("foodbutton");
        button.value = "ON";
        foodCheck.checked = true;
        button.style = "background-color: #d32323; color: white";
        restbutton.value = "OFF";
        restCheck.checked = false;
        restbutton.style = "background-color: lightgray; color: black";
    };
}