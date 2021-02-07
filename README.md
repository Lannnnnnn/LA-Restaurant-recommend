# DSC180B Project yelp-recommender-system

## We use the Autophrase as our core NLP analysis method and the original repository for AutoPhrase is linked by submodule: 
https://github.com/shangjingbo1226/AutoPhrase.

## AutoPhrase: Automated Phrase Mining from Massive Text Corpora

## Default Run

```
$ python3 run.py -- all
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- all
This will run all the targets below (data, eda, autophase, tokenize, result)

For each of the target:
* data: performs the data ingestion pipeline such as downloading the necessary data DBLP.txt
* tokenize: performs tokenization. It will take a raw train file and output a tokenization mapping for each detected token.
* eda: performs the eda analysis of the data file we used and some results.
* autophrase: runs the whole AutoPhrase algorithm. This target is used to run the whole process all at one time.
* result: performs result analysis and run a word2vec model.

```
$ python3 run.py -- data
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- data
* data will check if the test data exists and download the necessary file for analysis

```

```
$ python3 run.py -- eda
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- eda
* eda will produce the analysis of corpus data, model analysis and the comparison between different distributions of model output.
* we save the genreated image into the resources folder and our jupyter notebook will only show the result.

```
$ python3 run.py -- autophrase
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- autophrase
* autophrase will produce the final quality result by running the whole autophrase algorithm

```
$ python3 run.py -- tokenize
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- tokenize
* we will tokenize the input data text file

```
$ python3 run.py -- result
```
The default running file is run.py and can be simply run through the command line: python3 run.py -- result
* we will perform the result analysis and add to the notebook. 

## Result analysis

The result of AutoPhrase was analyzed in the notebook called Result.ipynb.

The first step we did was to extract 100 random samples from multi-word phrases output by AutoPhrase. This step was integrated into a method called "get_random" in the util.py file.

**Note:** DO NOT run the method because it will generate a list of words. Manually labeling them is PAINFUL!!!

After manually examine the 100 samples, we calculated the precision and recall pairs of the sample at different recall levels. We also plotted the precision-recall curve using a method called "plot_recall_precision".

Word2vec was used to do word-embedding and check the semantic similarity of the sampled phrases.

### Responsibilities

* Bingqi Zhou developed the the autophrase targets.
* Shenghan Liu developed data ingest, tokenize and eda targets and method files. He also created the submodule for AutoPhrase.
We both contributed to EDA and Result analysis.
