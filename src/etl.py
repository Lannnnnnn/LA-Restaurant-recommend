import os
import numpy as np
import shutil
import pandas as pd
import pdb
import json
import subprocess

import pyspark.ml as M
import pyspark.sql.functions as F
import pyspark.sql.types as T
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

ori_dir = "/AutoPhrase"
dir = os.getcwd()

spark = SparkSession \
    .builder \
    .appName("yelp-reccomender") \
    .getOrCreate()


def reviews_by_city(city_name, review_path, business_path):
    print(' --------Creating subset for: ' + city_name + ' --------')
    business_schema = T.StructType([
    #T.StructField("_c01", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("business_id", T.StringType(), True),   
    T.StructField("city", T.StringType(), True),   
    T.StructField("categories", T.StringType(), True),
    T.StructField("address", T.StringType(), True),
    T.StructField("review_count", T.IntegerType(), True),
    T.StructField("hours", T.StringType(), True),                  
    ])

    reviews_schema = T.StructType([
        #T.StructField("_c01", T.IntegerType(), True),
        T.StructField("review_id", T.StringType(), True),   
        T.StructField("business_id", T.StringType(), True),   
        T.StructField("text", T.StringType(), True),      
        T.StructField("stars", T.FloatType(), True),
        T.StructField("user_id", T.StringType(),  True),                  
    ])
    
    business = spark.read.csv("./data/raw/business.csv", header=True, multiLine=True, schema=business_schema, quote="\"", escape="\"")
    reviews = spark.read.csv("./data/raw/reviews.csv", header=True, multiLine=True, schema=reviews_schema, quote="\"", escape="\"")
    
    df = business.filter(business.city == city_name)\
.filter(business.categories.contains("Restaurants")|business.categories.contains('Food'))\
.join(reviews, business.business_id == reviews.business_id, 'inner')\
.drop(reviews.business_id)
#.drop(reviews._c01).drop(business._c01)
    
    res = df.toPandas().drop_duplicates(subset='review_id')
    
    res.to_csv('./data/tmp/' + city_name + '_subset.csv')
    
    with open('data/tmp/reviews/' + city_name + '.txt', 'w') as f:
        content = res['text'].str.cat(sep="\n<REVIEW_DELIMITER>\n")
        f.write(json.dumps(content))   

    print('Subset Created')
    
def autophrase_reviews(txt_list, path='data/tmp/reviews'):
    print('Starting AutoPhrase')
    try:
        shutil.copytree(path, dir + ori_dir + '/data/EN/reviews')
    except:
        shutil.rmtree(dir + ori_dir + '/data/EN/reviews')
        shutil.copytree(path, dir + ori_dir + '/data/EN/reviews')
    for name in txt_list:
        if name is not None:
            name += '.txt'
            with open(dir+ ori_dir + "/auto_phrase.sh",'r') as f , open(dir + ori_dir+ "/tmp_autophrase.sh",'w') as new_f:
                autophrased = [next(f) for x in range(146)] # get the autophase part
                index = 0
                for i in autophrased:
                    if index != 23:
                        new_f.write(i)
                    else:
                        new_f.write('DEFAULT_TRAIN=${DATA_DIR}/EN/reviews/' + name + '\n')
                    index += 1
            with open(dir+ ori_dir + "/phrasal_segmentation.sh",'r') as f , open(dir + ori_dir+ "/tmp_autophrase.sh",'a') as new_f:
                autophrased = [next(f) for x in range(90)] 
                index = 0
                new_f.write('\n')
                for i in autophrased:
                    if index != 14:
                        new_f.write(i)
                    else:
                        new_f.write('TEXT_TO_SEG=${TEXT_TO_SEG:- ${DATA_DIR}/EN/reviews/' + name + '}\n')
                    index += 1
        # change the access of the bash script
        os.chmod("./AutoPhrase/tmp_autophrase.sh", 509)
        os.chdir(dir + ori_dir)
        subprocess.run(["./tmp_autophrase.sh"])

        # move the result to the result folder
        shutil.copy(dir + ori_dir + '/models/DBLP/segmentation.txt', dir+ '/reference/AutoPhrase_result/' + name)
        os.chdir(dir)
        print('Autophrase for ' + name + ' is Done!')
            
    # remove the temporary bash script
    os.remove(dir + ori_dir + "/tmp_autophrase.sh")
    shutil.rmtree(dir + ori_dir + '/data/EN/reviews')
    return
    

def split_testdata(test_txt, test_user, business_csv, test_review, **kwargs):
    '''Return txt back to rows, each row being a review'''
    with open(test_txt, 'r') as f:
#     with open('../../DSC180A-Project/data/in/yelp_reviews2.txt', 'r') as f:
        reviews_string = f.read()
        reviews_list = reviews_string.split("\\n<REVIEW_DELIMITER>\\n")
#         reviews_list = reviews_string.split("\n<<phrase>REVIEW_DELIMITER</phrase>>\n")
#         reviews_list = reviews_string.split("\n.\n")

    reviews_list = pd.Series(reviews_list)[:-1] # last entry is always empty
    dtypes = {
        'review_id' : np.str,
        'business_id': np.str,
        'text': np.str,
        'stars': np.float64,
        'user_id': np.str
        
    }
    return reviews_list , pd.read_csv(test_user, dtype = dtypes), pd.read_csv(business_csv), pd.read_csv(test_review)

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
    if os.path.isdir('data/tmp') is False:
        command = 'mkdir -p ' + 'data/tmp'
        os.system(command)
    if os.path.isdir('data/tmp/reviews') is False:
        command = 'mkdir -p ' + 'data/tmp/reviews'
        os.system(command)
    if os.path.isdir('../AutoPhrase/data/EN/reviews') is False:
        command = 'mkdir -p ' + '../AutoPhrase/data/EN/reviews'
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