function generate_results() {
    document.querySelectorAll('.result_div').forEach(e => e.remove());
    document.querySelectorAll('.result_sep').forEach(e => e.remove());
    fetch('test/testdata/testdata_business.csv').then(response => response.text()).then(data => {
        const lines = data.split(/\r\n|\n/);
        lines.splice(0, 1);
        lines.splice(lines.length-1, 1);
        /*console.log(lines)*/
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
            document.body.appendChild(elementSep);
        }
        /*data2 = lines.join('\n\n');*/
        /*console.log(data2);*/
        /*data3 = data2.split(',').join('\n');
        document.getElementById('output').textContent=data3;*/
        scrolldown();
    });
}

function scrolldown() {
    var first_result = document.getElementById("result_element");
    first_result.scrollIntoView();
}