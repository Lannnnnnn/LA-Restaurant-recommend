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
    food_query_path = './data/{0}.csv'.format(location)
    restaurant_query_path = './data/{0}_rest_info.csv'.format(location)
    
    if foodbtn == 'ON':
#         df = pd.read_csv('./data/restaurant_phrases.csv')
        df = pd.read_csv(food_query_path)
        if vegan == 'ON':
            df = df[df['categories'].str.contains('Vegetarian')]

        df['phrases'] = df['phrases'].apply(lambda x: json.loads(x))
        
        df['stars'] = df['stars'].apply(lambda x: round(x, 1))
        

        df = df.assign(numMentions=df['phrases']\
        .apply(lambda x: find_substring(x, text)))\
        .dropna()\
        .sort_values(by='numMentions', ascending=False)

        df = df.assign(goodService=df['phrases']\
        .apply(lambda x: find_substring(x, "service")))\
        .sort_values(by=['numMentions', 'stars'], ascending=False)    

        return df.values.tolist()

    else:
        rest = pd.read_csv(restaurant_query_path)
        recomm_rest = []
        target_column = ['name','address','stars','review_count','categories','business_id']
        target_id_list = []
        index = 0
        for i in range(20):
            if index >= 5:
                break
            rank = 'Top_' + str(i)
            target_id = rest[rest.name == text][rank].value_counts().idxmax()
            if target_id in target_id_list:
                continue
            else:
                index += 1
                target_id_list.append(target_id)
                recomm_rest.append(rest[rest.business_id == target_id][target_column].values.tolist()[0])
        return recomm_rest
#     else:
#         with open('test/testdata/ph_testdata.csv', 'r') as f:
#             info = f.readlines()[1:]
#             for i in info:
#                 split_lines = i.replace('\n', '').replace('"', '').split(',')
#                 lines.append(split_lines)
#             return lines
        
        