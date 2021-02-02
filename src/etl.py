import pandas as pd
import os

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

def prepare_review_df(review, **kwargs):
    return pd.read_csv(review)
