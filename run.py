import sys
import os
import json
import pandas as pd

sys.path.insert(0, 'src')
from eda import *

eda_config = json.load(open('config/eda-params.json'))

def main(targets):
    if 'test' in targets:
        test_config = json.load(open('config/test-params.json'))
        df = pd.read_csv(test_config['testdata']).drop_duplicates()
        df['num_sentences'] = df['text'].apply(get_num_sentences)
        df['num_words'] = df['text'].apply(get_num_words)

        if not os.path.isdir('src/data'):
            os.makedirs('src/data')
            
        ax=df['stars'].value_counts().plot(kind='bar', title="Stars Histogram")
        ax.set_xlabel("Stars")
        ax.set_ylabel("Number of reviews")
        fig=ax.get_figure()
        destination = eda_config['output_dir'] + 'stars_bar.png'
        fig.savefig(destination)

        ax=df.plot.scatter(y='stars', x='num_sentences', title="Stars in relation to Number of Sentences")
        fig=ax.get_figure()
        destination = eda_config['output_dir'] + 'num_sent_scatter.png'
        fig.savefig(destination)

        ax=df.plot.scatter(y='stars', x='num_words', title="Stars in relation to Number of words")
        fig=ax.get_figure()
        destination = eda_config['output_dir'] + 'num_words_scatter.png'
        fig.savefig(destination)

        ax = df['num_sentences'].hist()
        ax.set_xlabel("Number of sentences in the review")
        ax.set_ylabel("Number of reviews")
        fig=ax.get_figure()
        destination = eda_config['output_dir'] + 'num_sent.png'
        fig.savefig(destination)

        ax = df['num_words'].hist()
        ax.set_xlabel("Number of words in the review")
        ax.set_ylabel("Number of reviews")
        fig=ax.get_figure()
        destination = eda_config['output_dir'] + 'num_words.png'
        fig.savefig(destination)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)