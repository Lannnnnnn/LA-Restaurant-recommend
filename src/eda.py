import os
from collections import defaultdict
import re
import json

def save_eda_data(df, positive_phrases, negative_phrases, outdir):
    '''Save the sentiment output in outdir for eda.'''
    if os.path.isdir(outdir) is False:
        command = 'mkdir -p ' + outdir
        os.system(command)
    
    df.to_csv(outdir + '/restaurant.csv')
    positive_phrases.to_csv(outdir + '/positive.csv')
    negative_phrases.to_csv(outdir + '/negative.csv')
    
    return