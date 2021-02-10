fetch('test/testdata/testdata_business.csv').then(response => response.text()).then(data => {
    const lines = data.split(/\r\n|\n/);
    lines.splice(0, 1);
    lines.splice(lines.length-1, 1);
    /*console.log(lines)*/
    var i;
    for (i=0;i<lines.length;i++) {
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
        newElement.id = lines[i];
        newElement.innerHTML = lines[i];
        document.body.appendChild(newElement);
        document.body.appendChild(document.createElement('br'))
    }
    /*data2 = lines.join('\n\n');*/
    /*console.log(data2);*/
    /*data3 = data2.split(',').join('\n');
    document.getElementById('output').textContent=data3;*/
});