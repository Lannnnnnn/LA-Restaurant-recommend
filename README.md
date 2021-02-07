# DSC180B Project yelp-recommender-system

## Important Things:
* This repository is contains one main branch and three split branches owned by each of the project team members. Make sure git clone the main branch and run!
* In our implmentation and analysis, we use the Autophrase as our core NLP analysis method by submoduling into our repository.
- If you would like to learn more details about the AutoPhrase method, please refer to the original github repository: https://github.com/shangjingbo1226/AutoPhrase. Namely, you will find the system requirements, all the tools used and detailed explanation of the output.
- Jingbo Shang, Jialu Liu, Meng Jiang, Xiang Ren, Clare R Voss, Jiawei Han, "**[Automated Phrase Mining from Massive Text Corpora](https://arxiv.org/abs/1702.04457)**", accepted by IEEE Transactions on Knowledge and Data Engineering, Feb. 2018.

## Default Run

```
$ python3 run.py -- all
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- all
This will run all the targets below (data, sentiment, eda, test, clean)

For each of the target:
* data: performs the data ingestion pipeline such as downloading the necessary data, read the necessary configuration
* sentiment: performs sentiment analysis on the reviews. It will take in the reviews dataframe and output the positive/negative sentences counts.
* eda: performs the eda analysis of the dataset and autophrase result.
* test: runs the whole process on a test dataset which runs around 3mins.
* clean: removes all the files generated with keeping the html report in the data/eda folder.

```
$ python3 run.py -- data
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- data
* Check if the reference folder exists in the user local drive. If not, create all the necessary folder for projects
* Read the dataframes for further analysis.
* download the large dataset for completely running the project. (future work)

```
$ python3 run.py -- sentiment
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- sentiment
* Perform sentiment analysis on the reviews text
* Output that has the sentiment of each sentence in the review with its extracted phrases will be stored in the data/tmp folder

```
$ python3 run.py -- eda
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- eda
* Perform the EDA analysis on the AutoPhrase result of individual user
* Perform the EDA analysis on individual city review dataset such as sentiment analysis, feature exploration
* Convert all the EDA analysis into an HTML report stored under data/eda
* After running this tag go to the data/eda directory to see the report.html

```
$ python3 run.py -- TF-IDF (not implmented yet)
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- TD-IDF
* Run the user-user based and item-item based recommendation methods using TF-IDF and cosine similarity score
* Given a user or a restaurant, recommend a list of most related user / restaurant based on cosine similarity score


```
$ python3 run.py -- clean
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- clean
* Remove all the generated files, plots, dataframes under the reference folder
* Keep the HTML file in the eda/data folder for report visualization
* Be careful: this will clear all the outputs running so far and can not be reversed!!

```
$ python3 run.py -- test
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- test
* Run all the targets on the test data set we generated 

## Future Design

- We start designing the website for deploying our recommendation system and the skeleton will be finished by week 6.
- We are implmenting more advanced recommendation methods such as ALS and explore the system to our whole dataset instead of certain city.


### Responsibilities
* Catherine Hou developed the sentiment tag and eda tag.
* Vincent Le created the dockerfile and developed the website skeleton (not yet in main branch).
* Shenghan Liu developed TF-IDF algorithm, user AutoPhrase EDA, data tag. Clean, merge the branches and write the first readme draft.
