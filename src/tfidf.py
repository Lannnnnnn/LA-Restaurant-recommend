import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

def tf_idf_on_user(reviews, business_df, amount = 5):
    print('-------- Running TF-IDF Recommendation method --------')
    user_df = preprocess_group_user_review(reviews)
    rest_df = preprocess_group_restaurant_review(reviews, business_df)
    user_feature_matrix = generate_user_matrix(user_df, 'user_id')
    rest_feature_matrix = generate_user_matrix(rest_df, 'business_id')
    
    # generate a random user id and random restaurant business id, store their indexs in the reference folder
    random_user = user_df.iloc[len(user_df)//2].user_id
    user_df[user_df.user_id == random_user].to_csv('./reference/dataframe/user_index.csv')
    random_rest = rest_df.iloc[len(rest_df)//2].business_id
    reviews[reviews.business_id == random_rest][['business_id','name','categories']].head(1).reset_index().to_csv('./reference/dataframe/rest_index.csv')
    
    # make recommendation based on the random rest and user id, store the recommendation list in the reference folder
    make_recommendations(random_user, user_feature_matrix, user_df[['user_id','text', 'categories']], k=amount).to_csv(
    './reference/dataframe/user_recommendation.csv')
    make_recommendations(random_rest, rest_feature_matrix, reviews[['name','business_id','categories']], k=amount).to_csv(
    './reference/dataframe/restaurant_recommendation.csv')
    print('storing the result dataframe into reference folder...')
    print('------- TF-IDF Recommendation method finished --------')
    return 

def preprocess_group_user_review(review_df):
    user_df = review_df[['text','categories','user_id']].groupby('user_id').agg({'text':list,
                                                                            'categories':lambda column: ' '.join(column)}
                                                                          ).reset_index()
    user_df.text = user_df.text.apply(lambda t: "".join(re.sub(r'[^\w\s]',' ',str(t))).replace("\n"," "))
    return user_df

def preprocess_group_restaurant_review(review_df, business_df):
    restaurant_df = review_df[['text','stars','business_id']].groupby('business_id').agg({'text':list,
                                                                                          'stars':np.mean}
                                                                                        ).reset_index()
    restaurant_df.text = restaurant_df.text.apply(lambda t: "".join(re.sub(r'[^\w\s]',' ',str(t))).replace("\n"," "))
    return restaurant_df.merge(business_df[['name', 'business_id']], on = 'business_id')

def generate_user_matrix(grouped_df, index_column):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(grouped_df.text.apply(lambda x: x.lower()))
    cosine_sim = cosine_similarity(tfidf_matrix)
    if index_column == 'user_id':
        return pd.DataFrame(cosine_sim, columns=grouped_df.user_id, index=grouped_df.user_id)
    else:
        return pd.DataFrame(cosine_sim, columns=grouped_df.business_id, index=grouped_df.business_id)

def make_recommendations(ID, df, record, k=10):
    """
    Recommends user based on a similarity dataframe
    Parameters
    ----------
    ID : str
        User ID (index of the similarity dataframe)
    df : pd.DataFrame
        Similarity dataframe, symmetric, with movies as indices and columns
    record : pd.DataFrame
        The record of original user and some other features used to define similarity
    k : int
        Amount of recommendations to return
    """
    ix = df.loc[:,ID].to_numpy().argpartition(range(-1,-k,-1))
    high_recomm = df.columns[ix[-1:-(k+2):-1]]
    high_recomm = high_recomm.drop(ID, errors='ignore')
    return pd.DataFrame(high_recomm).merge(record).drop_duplicates().head(k)
