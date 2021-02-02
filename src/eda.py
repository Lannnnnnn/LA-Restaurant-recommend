from util import *

def save_eda(review):
    user_review_count_df, picked_user = user_distribution(review)
    for i in picked_user[0]:
        fname, fpath = generate_user_review_txt(i, review)
        run_autophrase(fname)
    
    # save the user review count dataframe
    user_review_count_df.to_csv("./reference/dataframe/user_review_count.csv")
    
    return