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

data_config = json.load(open('config/data-params.json'))

def main(targets):
    if ('sentiment' or 'all') in targets:
        reviews_list = split_data(data_config['outdir'])
        df = sentiment.make_sentiment_table(reviews_list)
    if 'test' in targets:
        reviews_list = split_data('test/testdata/annotated_test.txt')
        df, positive_phrases, negative_phrases = make_sentiment_table(reviews_list)
        pdb.set_trace()
    return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)