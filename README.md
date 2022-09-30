# What are the discriminative features?

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

Choose the *data sets* you want to work with.

1. (stInfo) `studentInfo.csv`: use `display_stInfo.ipynb`.
2. (stAll) `studentInfo.csv`, `studentAssessment.csv`, `assessments.csv`, and `studentVle.csv`(add scores and clicks): use `merging.ipynb` and `display_stAll.ipynb`.

Execute all the preprocessing steps (also using `encode_features.py`):
```
python3 preprocessing_data.py
```

