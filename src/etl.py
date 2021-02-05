import pandas as pd
import os
import numpy as np
import shutil

def check_result_folder(out_df, out_img, out_txt, **kwargs):
    # create the result placement folder if does not exist
    if os.path.isdir(out_df) is False:
        command = 'mkdir -p ' + out_df
        os.system(command)
    if os.path.isdir(out_img) is False:
        command = 'mkdir -p ' + out_img
        os.system(command)
    if os.path.isdir(out_txt) is False:
        command = 'mkdir -p ' + out_txt
        os.system(command)
    return

def prepare_review_df(path):
    dtypes = {
        'review_id' : np.str,
        'business_id': np.str,
        'text': np.str,
        'stars': np.float64,
        'user_id': np.str
        
    }
    return pd.read_csv(path, dtype = dtypes)

def clean_repo():
    if os.path.isdir('reference') is True:
        shutil.rmtree('reference')
    if os.path.isdir('originalAutoPhrase/tmp') is True:
        shutil.rmtree('originalAutoPhrase/tmp')
    if os.path.isdir('tmp') is True:
        shutil.rmtree('tmp')
    return
