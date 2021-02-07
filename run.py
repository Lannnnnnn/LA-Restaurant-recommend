import sys
import os
import json
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sys.path.insert(0, 'src')
from sentiment import *
from etl import *
from eda import *
from utils import *

data_config = json.load(open('config/data-params.json'))
eda_config = json.load(open('config/eda-params.json'))

def main(targets):
    
    # data ingestion not implmented yet
    if ('data') in targets:
        check_result_folder(**eda_config)
        reviews_list = split_data(data_config['outdir'], data_config['review'])
    
    if ('sentiment' or 'all') in targets:
        df = make_sentiment_table(reviews_list)
        df, positive_phrases, negative_phrases = make_sentiment_table(reviews_list)
        
    if ('eda' or 'all') in targets:
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['outdir'], eda_config['out_txt'], review)
        convert_eda(**eda_config)
        
    if ('clean') in targets:
        clean_repo()
        
    if 'test' in targets:
        check_result_folder(**eda_config)
        test_reviews_list, test_review = split_data(data_config['test_txt'], data_config['test_review'])
        df, positive_phrases, negative_phrases = make_sentiment_table(test_reviews_list)
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['out_df'], eda_config['out_txt'], test_review)
        convert_eda(**eda_config)
        return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)