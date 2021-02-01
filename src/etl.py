import pandas as pd
import pdb

def split_data(path):
    '''Return txt back to rows, each row being a review'''
    with open(path, 'r') as f:
#     with open('../../DSC180A-Project/data/in/yelp_reviews2.txt', 'r') as f:
        reviews_string = f.read()
        reviews_list = reviews_string.split("\n<REVIEW DELIMITER>\n")
#         reviews_list = reviews_string.split("\n.\n")
        
    reviews_list = pd.Series(reviews_list)[:-1] # last entry is always empty
    return reviews_list