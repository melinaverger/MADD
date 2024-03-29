# *Model Absolute Density Distance* (MADD), metric and post-processing

[![Generic badge](https://img.shields.io/badge/python-3.10.4-green.svg)](https://shields.io/)

This repository contains all the source code of the experiments that were done in the papers of the [References](../README.md#references) section.

## 1. Set up the project on your computer

**N. B.:** We did not use a Python package manager (e.g. Anaconda) other than the package installer [pip](https://pip.pypa.io/en/latest/). Plus, [Git](https://git-scm.com) should be installed on your computer.

Clone this repository, either by `git clone` command line or by download the repository manually.

Change your current working directory to your local repository with `cd` command line such as:
```
$ cd <path of the repository>
```

Then, download the needed packages to run all scripts using the following command line (we suggest you create a local virtual environment beforehand):
```
$ pip install -r requirements.txt  
```

## 2. Start the project

**N. B.:** The outcomes of this section should already be computed and available in the `data` and `preparation` folders. You can skip this section to go directly to the next one. However, we let the following instructions anyway in case you want to start the projet from scratch.

First of all, go to `preparation` folder.

### 2.1. Loading data

#### a) Data sets

If you do not already have the OULAD data sets on your computer, run the following (assuming you have [Python 3](https://www.python.org/downloads/) installed):
```
$ python3 load_data.py
```

#### b) Get to know the sets

Then, to explore and to have an idea about the different sets, run `display_sets.ipynb`.

### 2.2. Preprocessing

Choose the *data sets* you want to work with. Either:
1. (stInfo) `studentInfo.csv`: use `display_stInfo.ipynb`, or,
2. (stAll) `studentInfo.csv`, `studentAssessment.csv`, `assessments.csv`, and `studentVle.csv` (adding scores and clicks): use `merging_stAll.ipynb` and `display_stAll.ipynb`, or,
3. (stClick) `studentInfo.csv`, and `studentVle.csv` (adding clicks): use `merging_and_display_stClick.ipynb`.

Then, execute all the preprocessing steps (that use `encode_features.py`) by running:
```
/!\ You will have to make some data cleaning decisions.

$ python3 preprocessing_data.py
```

You can check the scaling step results by running `check_scaling_data.ipynb`.

You now have a data set ready for analyses and to start machine learning.

## 3. Features analysis

To plot different information for feature analysis, do "Run All" into `feature_analysis.ipynb`.

## 4. Machine learning pipeline and algorithmic fairness analyses

Run all `pipeline.ipynb`. You will have to enter:
* the data set you chose,
* if you want to reduce your data set to course 'BBB' or course 'FFF' data,
* the train-test split ratio you want between 70-30 or 80-20,
* the sensitive attributes you should have identified,
* the classifier models to study.

By running all `pipeline.ipynb`, it will also automatically run:
* `dataviz.ipynb`: to inspect the training set,
* `eval_performance.ipynb`: to test the trained models and return their accuracies (and optionally their feature importance),
* `eval_fairness_madd.ipynb`: to compute the Model Absolute Density Distance (MADD) for all models and all sensitive attributes,
* `eval_fairness_plots`: to visualize the models' discriminatory behaviors (visual inspections of MADD results) through their [Kernel Density Estimation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html)s,
* `abroca.ipynb`: to compute and visualize the  Absolute Between-ROC Area (ABROCA) for all models and all sensitive attributes.

**N. B.:** The outputs of these notebooks are visible in their associated `nbconvert.ipynb` notebook versions.
