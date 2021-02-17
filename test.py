def test_function(text, location, foodbtn):
    lines = []
    if location == "Las Vegas":
        with open('test/testdata/lv_testdata.csv', 'r') as f:
            info = f.readlines()[1:]
            for i in info:
                split_lines = i.replace('\n', '').replace('"', '').split(',')
                lines.append(split_lines)
            return lines
    else:
        with open('test/testdata/ph_testdata.csv', 'r') as f:
            info = f.readlines()[1:]
            for i in info:
                split_lines = i.replace('\n', '').replace('"', '').split(',')
                lines.append(split_lines)
            return lines