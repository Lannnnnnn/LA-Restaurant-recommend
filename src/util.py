import os
import shutil
import sys
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns 

ori_dir = "/originalAutoPhrase"
dir = os.getcwd()

def user_distribution(review):
    """
    generate the user review distribution for 20 most review and the overall distribution of reviews
    
    return a list of user id includes the most and second most reviews user,
             user id with 100<review<1000, user id with review < 100
    """
    user_review_count_df = review.user_id.value_counts().sort_values(ascending=False)
    
    # generate the user distribution plot
    x = user_review_count_df.iloc[0:20] 
    plt.figure(figsize=(16,4))
    ax = sns.barplot(x.index, x.values, alpha=0.8)
    plt.title("20 Users with Most Reviews ")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.ylabel('number of reviews', fontsize=12)
    plt.xlabel('User', fontsize=12)

    # adding the text labels
    rects = ax.patches
    labels = x.values
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
    
    print('save the user distribution image now')
    plt.savefig("./reference/img/most_20_user.png")
    
    user_list = [user_review_count_df.index[0], user_review_count_df.index[1],
                 a[(a.values > 100) & (a.values < 1000)].index[0], a[(a.values <= 100)].index[0]]
    return pd.DataFrame({'user_id':user_review_count_df.index, 'count':user_review_count_df.values}), user_list

def generate_user_review_txt(user_id, reviews):
    '''
    generate the txt file that contains all reviews of a user
    @param user_id: string of the user unique id
    @param reviews: all reviews csv file
    @return: the file path that store the txt file
    '''
    # filter out the user review record from all reviews
    user_df = reviews.loc[reviews['user_id'] == user_id]
    
    # if the user does not have any reviews before
    if not len(user_df):
        print('The user does not have any previous review record')
        return 
    
    print('generate the txt file for User' + user_id) 
    
    # store the user reviews txt file under the src/user_reviews folder
    file_path = 'reference/user_reviews/' + user_id + '.txt'
    user_df[['text']].to_csv(file_path, header=None, index=None, sep=',', mode='a')   
    return user_id + '.txt', file_path

def run_autophrase(txt_name, path = '/reference/user_reviews/'):
    shutil.copy(path + txt_name, dir + ori_dir + '/data/' + txt_name)
    with open(dir+ ori_dir + "/auto_phrase.sh",'r') as f , open(dir + ori_dir+ "/tmp_autophrase.sh",'w') as new_f:
        autophrased = [next(f) for x in range(146)] # get the autophase part
        index = 0
        for i in autophrased:
            if index != 23:
                new_f.write(i)
            else:
                new_f.write('DEFAULT_TRAIN=${DATA_DIR}/' + txt_name + '\n')
            index += 1
    # change the access of the bash script
    os.chmod("./originalAutoPhrase/tmp_autophrase.sh", 509)
    os.chdir(dir + ori_dir)
    subprocess.run(["./tmp_autophrase.sh"])
    
    # move the result to the result folder
    shutil.copytree(dir + ori_dir + '/tmp', dir+'/tmp')
    
    # remove the temporary bash script
    os.remove(dir + ori_dir + "/tmp_autophrase.sh")
    os.chdir(dir)
    print('Autophrase for' + txt_name + 'is Done!')
    return