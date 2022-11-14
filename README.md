# What are the discriminative features?

[![Generic badge](https://img.shields.io/badge/python-3.10.4-green.svg)](https://shields.io/)

## 1. To use the project on your local computer

Clone the repository and use the following command line to download the needed packages:
```
pip install -r requirements.txt
```

Then, activate the virtual environment `env` (and enter `deactivate` when you quit):
```
source env/bin/activate
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
2. (stAll) `studentInfo.csv`, `studentAssessment.csv`, `assessments.csv`, and `studentVle.csv` (adding scores and clicks): use `merging_stAll.ipynb` and `display_stAll.ipynb`, or,
3. (stClick) `studentInfo.csv`, and `studentVle.csv` (adding clicks): use `merging_stClick.ipynb`.

Then, execute all the preprocessing steps (that use `encode_features.py`) by runing:
```
python3 preprocessing_data.py
```

You can check the scaling step by runing `check_scaling_data.ipynb`.

You have now a data set ready for analyses and machine learning.

## 3. Features analysis

To plot different information for feature analysis, do "Run All" into `features_analysis.ipynb`.

## 4. Machine learning pipeline

Run `train_test_split_and_models.ipynb` and it will launch the following notebooks in this order:

`train_test_split_and_models.ipynb`: to prepare the chosen data set until train-test split.  
-> It is here to coose if you want to limit the data to course 'BBB' for instance.  
-> The resulting train and test sets settings along with the split ratio are saved in `DATA` and `SPLIT` files in `./data` folder. You do not need to specify the chosen set and ratio for the other notebooks.  
-> It is also here to specificy the sensitive features you choose.  
-> It is also here to select and train the classifier models you want to work with. The trained models are saved in `./models` folder.

`eval_performance.ipynb`: to test the trained models and return their accuracies and feature importance.

`eval_fairness.ipynb`: to evaluate algorihtmic fairness of the trained models.

**N. B.:** To see the outpus, look into each associated `nbconvert.ipynb`notebook.

### 4. Qualitative and quantitavie algorithmic fairness analyses

This section is dedicated to data distribution comparisons.

Run the following notebooks in this order.

`distrib_plots.ipynb`: to plot the data distributions of the choosen sensitive features (including their [Kernel Density Estimation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html)).

`distrib_measure.ipynb`

**N. B.:** To see the outpus, look into each associated `nbconvert.ipynb`notebook.

### 5. Data vizualisation

Since you have saved a training set, you can now explore this set and only this one via `dataviz.ipynb`.
