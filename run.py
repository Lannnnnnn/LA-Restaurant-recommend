import sys
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
        df = prepare_review_df(data_config['review'])
        save_eda(df)
                   
    if 'test' in targets:
        check_result_folder(**eda_config)
        test_df = prepare_review_df(data_config['test_review'])
        save_eda(test_df)
    
    if 'clean' in targets:
        clean_repo()
    return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)