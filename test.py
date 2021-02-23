import pandas as pd

def test_function(text, location, foodbtn, vegan):
    lines = []
    if location == "Las Vegas":
        if foodbtn == 'ON':
            with open('test/testdata/lv_testdata.csv', 'r') as f:
                info = f.readlines()[1:]
                for i in info:
                    split_lines = i.replace('\n', '').replace('"', '').split(',')
                    lines.append(split_lines)
            return lines
        else:
            rest = pd.read_csv('test/testdata/LV_rest_info.csv')
            recomm_rest = []
            target_column = ['name','business_id','categories','stars']
            for i in range(5):
                rank = 'Top_' + str(i)
                target_id = rest[rest.name == "Carl's Jr"][rank].value_counts().idxmax()
                recomm_rest.append(rest[rest.business_id == target_id][target_column].values.tolist()[0])
            return recomm_rest
    else:
        with open('test/testdata/ph_testdata.csv', 'r') as f:
            info = f.readlines()[1:]
            for i in info:
                split_lines = i.replace('\n', '').replace('"', '').split(',')
                lines.append(split_lines)
            return lines