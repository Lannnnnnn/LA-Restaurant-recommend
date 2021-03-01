import pandas as pd
import pdb
import json

def find_substring(record, query):
    res = 0
    for key, value in record.items():
        if query in key:
            res += value
    return res

def test_function(text, location, foodbtn, vegan):
    lines = []
    location = location.replace(' ', '_')
    restaurant_path = './data/{0}.csv'.format(location)
    if foodbtn == 'ON':
#         df = pd.read_csv('./data/restaurant_phrases.csv')
        df = pd.read_csv(
        if vegan == 'ON':
            df = df[df['categories'].str.contains('Vegetarian')]

        df['phrases'] = df['phrases'].apply(lambda x: json.loads(x))

        df = df.assign(numMentions=df['phrases']\
        .apply(lambda x: find_substring(x, text)))\
        .dropna()\
        .sort_values(by='numMentions', ascending=False)

        df = df.head()

        df['stars'] = df['stars'].apply(lambda x: round(x, 1))

        df = df.assign(goodService=df['phrases']\
        .apply(lambda x: find_substring(x, "service")))\
        .sort_values(by='numMentions', ascending=False)    

        return df.values.tolist()

    else:
        rest = pd.read_csv('test/testdata/LV_rest_info.csv')
        recomm_rest = []
        target_column = ['name','address','stars','review_count','categories']
        for i in range(5):
            rank = 'Top_' + str(i)
            target_id = rest[rest.name == text][rank].value_counts().idxmax()
            recomm_rest.append(rest[rest.business_id == target_id][target_column].values.tolist()[0])
        return recomm_rest
    else:
        with open('test/testdata/ph_testdata.csv', 'r') as f:
            info = f.readlines()[1:]
            for i in info:
                split_lines = i.replace('\n', '').replace('"', '').split(',')
                lines.append(split_lines)
            return lines
        
        