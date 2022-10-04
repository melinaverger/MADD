# What are the discriminative features?

[![Generic badge](https://img.shields.io/badge/python-3.10.4-green.svg)](https://shields.io/)

## 1. To use the project on your local computer

Clone the repository and use the following command line to download the needed packages:
```
pip install -r requirements.txt
```

## 2. Start the project

### 2.1. Loading data

#### Data sets

If you did not have the OULAD data sets, run the following (assuming you have [Python 3](https://www.python.org/downloads/) installed):
```
python3 load_data.py
```

#### Get to know the sets

Then, to explore the different sets, run `display_set.ipynb`.

### 2.2. Preprocessing

Choose the *data sets* you want to work with, either:
1. (stInfo) `studentInfo.csv`: use `display_stInfo.ipynb`, or,
2. (stAll) `studentInfo.csv`, `studentAssessment.csv`, `assessments.csv`, and `studentVle.csv`(adding scores and clicks): use `merging.ipynb` and `display_stAll.ipynb`.

Then, execute all the preprocessing steps (that use `encode_features.py`) by runing:
```
python3 preprocessing_data.py
```

You can check the scaling step by runing `check_scaling_data.ipynb`.

You have now a data set ready for analyses and machine learning.

## 3. Features analysis

To plot different information for feature analysis, do "Run All" into `features_analysis.ipynb`.

## 4. Machine learning pipeline

### 4...
You will have the plots only when you will run `experiment1.ipynb` since we need to do data vizualisation only on the training sets. See them into `dataviz.ipynb`.


