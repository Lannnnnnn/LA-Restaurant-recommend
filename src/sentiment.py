import json
import os
import numpy as np
import pandas as pd
import re

import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import pdb

def sentiment_score(reviews_list):
    '''Attach a sentiment score to each sentence of a review. Return DataFrame.'''
    scores = []
    seen_sentences = []
    index = []
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sid = SentimentIntensityAnalyzer()
    for i, review in enumerate(reviews_list):
        sentences = tokenizer.tokenize(review)
        for sentence in sentences:
            index.append(i)
            seen_sentences.append(sentence)
            ss_intermediate = sid.polarity_scores(sentence)
            scores.append(ss_intermediate)
    df = pd.DataFrame({'index': index, 'sentence': seen_sentences}).join(pd.DataFrame(scores))
    df = df.assign(phrases = df.sentence.apply(lambda x: re.findall('<phrase>.+?</phrase>', x)))
    return df

def clean_phrases(sentences):
    '''Remove the phrase tags'''
    return sentences.str.replace('<phrase>', '').str.replace('</phrase>', '')

def make_positive_phrases(df, val):
    '''Return positive phrases'''
    return clean_phrases(df[['compound', 'phrases']][df['compound']>=val].phrases.explode().dropna()).value_counts()

def make_negative_phrases(df, val):
    '''Return positive phrases'''
    return clean_phrases(df[['compound', 'phrases']][df['compound']<=-val].phrases.explode().dropna()).value_counts()

def make_sentimented_restaurant(reviews_list, VAL):
    '''Return a dataframe '''
    df = sentiment_score(reviews_list)
    positive_phrases = make_positive_phrases(df, VAL)
    negative_phrases = make_negative_phrases(df, VAL)
    df = df.assign(positive)

def make_sentiment_table(reviews_list):
    '''Return a table with sentiment per sentence; positive phrases; negative phrases'''
    VAL = 0.3
    df = sentiment_score(reviews_list)
    positive_phrases = make_positive_phrases(df, VAL)
    negative_phrases = make_negative_phrases(df, VAL)
    return df, positive_phrases, negative_phrases
    