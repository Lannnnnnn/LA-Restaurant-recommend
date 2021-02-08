import os
import numpy as np
import shutil
import pandas as pd
import pdb

def split_data(test_txt, test_review, business_csv, test_grouped_review, **kwargs):
    '''Return txt back to rows, each row being a review'''
    with open(test_txt, 'r') as f:
#     with open('../../DSC180A-Project/data/in/yelp_reviews2.txt', 'r') as f:
        reviews_string = f.read()
        reviews_list = reviews_string.split("\n<REVIEW DELIMITER>\n")
#         reviews_list = reviews_string.split("\n.\n")
        
    reviews_list = pd.Series(reviews_list)[:-1] # last entry is always empty
    dtypes = {
        'review_id' : np.str,
        'business_id': np.str,
        'text': np.str,
        'stars': np.float64,
        'user_id': np.str
        
    }
    return reviews_list , pd.read_csv(test_review, dtype = dtypes), pd.read_csv(business_csv), pd.read_csv(test_grouped_review)

def check_result_folder(out_df, out_img, out_txt, out_autophrase, **kwargs):
    # create the result placement folder if does not exist
    print(' --------Checking the reference folder now ------')
    if os.path.isdir(out_df) is False:
        command = 'mkdir -p ' + out_df
        os.system(command)
    if os.path.isdir(out_img) is False:
        command = 'mkdir -p ' + out_img
        os.system(command)
    if os.path.isdir(out_txt) is False:
        command = 'mkdir -p ' + out_txt
        os.system(command)
    if os.path.isdir(out_autophrase) is False:
        command = 'mkdir -p ' + out_autophrase
        os.system(command)
    print(' --------The reference folder is ready ------')
    return

def clean_repo():
    if os.path.isdir('reference') is True:
        shutil.rmtree('reference')
    if os.path.isdir('AutoPhrase/tmp') is True:
        shutil.rmtree('AutoPhrase/tmp')
    if os.path.isdir('tmp') is True:
        shutil.rmtree('tmp')
    if os.path.isdir('AutoPhrase/data/txt') is True:
        shutil.rmtree('AutoPhrase/data/txt')
    return