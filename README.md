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

`train_test_split.ipynb` -> DATA SPLIT saved

`models_training.ipynb` -> models saved

`eval_performance.ipynb` -> predictive performance + FI

`eval_fairness.ipynb` -> 


(Old)
Run `experiment.ipynb` and choose either you want to work with course 'BBB' data only or with the whole the data set, and choose the train-test split ratio between 70-30 and 80-20.

The train and test sets are saved in `./data` folder, and the trained models are saved in `./models` folder.

Some feature importance information are displayed in the notebook. 

### 4. Data vizualisation

Since you have saved a training set, you can now explore this set and only this one via `dataviz.ipynb`.


