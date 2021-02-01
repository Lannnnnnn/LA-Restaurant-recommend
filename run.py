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
    if ('sentiment' or 'all') in targets:
        reviews_list = split_data(data_config['outdir'])
        df = sentiment.make_sentiment_table(reviews_list)
        df, positive_phrases, negative_phrases = make_sentiment_table(reviews_list)
    if ('eda' or 'all') in targets:
        save_eda_data(df, positive_phrases, negative_phrases, eda_config['outdir'])
        convert_eda(**eda_config)
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