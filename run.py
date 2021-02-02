import sys
import os
import json

sys.path.insert(0, 'src')
from etl import *
from eda import *
from util import *

# load the json file
data_config = json.load(open('config/data-params.json'))
eda_config = json.load(open('config/eda-params.json'))

def main(targets):
    if ('eda' or 'all') in targets:
        check_result_folder(**eda_config)
        df = prepare_review_df(**data_config)
        run_eda(df)
        
                
    if 'test' in targets:
        reviews_list = split_data('test/testdata/annotated_test.txt')
        df, positive_phrases, negative_phrases = make_sentiment_table(reviews_list)
        convert_eda(**eda_config)
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['outdir'])
    return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)