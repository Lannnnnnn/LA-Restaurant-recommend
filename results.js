fetch('test/testdata/lv_test_data.csv').then(response => response.text()).then(data => {
    const lines = data.split(/\r\n|\n/);
    data2 = lines.join('\n\n');
    console.log(data2);
    document.getElementById('output').textContent=data2;
});