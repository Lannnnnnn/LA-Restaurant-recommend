import sys
import os
import json
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt', quiet=True)
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sys.path.insert(0, 'src')
from sentiment import *
from etl import *
from eda import *
from utils import *
from tfidf import *

data_config = json.load(open('config/data-params.json'))
eda_config = json.load(open('config/eda-params.json'))

def main(targets):
    
    # data ingestion not implmented yet
    if ('data') in targets:
        check_result_folder(**eda_config)
        reviews_by_city(city_name=data_config['city_name'], review_path=data_config['review'], business_path=data_config['business_csv'])
        autophrase_reviews(txt_list=[data_config['city_name']])
        test_reviews_list, test_review, business_df, test_grouped_review = split_data(**data_config)
    
    if ('sentiment' or 'all') in targets:
        test_reviews_list, test_review, business_df, test_grouped_review = split_data(**data_config)
        # df = make_sentiment_table(test_reviews_list)
        df, positive_phrases, negative_phrases = make_sentiment_table(test_reviews_list, data_config['restaurant_dir'])
        make_website_table(df, data_config["restaurant_dir"], data_config["subset_dir"])
        
    if ('tfidf' or 'all') in targets:
        tf_idf_on_user(test_grouped_review, business_df, amount = 4)
        
    if ('eda' or 'all') in targets:
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['outdir'], eda_config['out_txt'], review)
        convert_eda(**eda_config)
    
    if ('clean') in targets:
        clean_repo()
        
    if 'test' in targets:
        check_result_folder(**eda_config)
        
        reviews_by_city(city_name=data_config['city_name'], review_path=data_config['review_test'], business_path=data_config['business_csv_test'])
        autophrase_reviews(txt_list=[data_config['city_name']])

        data_config['business_csv'] = data_config['business_csv_test']

        test_reviews_list, test_review, business_df, test_grouped_review = split_data(**data_config)
                
        df, positive_phrases, negative_phrases = make_sentiment_table(test_reviews_list, data_config['restaurant_dir'])
        make_website_table(df, data_config["restaurant_dir"], data_config["subset_dir"])
        
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['out_df'], eda_config['out_txt'], test_review)
        tf_idf_on_user(test_grouped_review, business_df, amount = 4)
        # convert_eda(**eda_config)
        return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)