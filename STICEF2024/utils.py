import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score


def show_accuracy(model, model_name, X_train, X_test, y_train, y_test):
    NB_FOLD = 5
    scores_train = cross_val_score(model, X_train, y_train, cv=NB_FOLD)
    print(f'===== {model_name} =====')
    print('Training set:', scores_train.mean(), scores_train.std())
    print('Test set:', accuracy_score(y_test, model.predict(X_test)))


def predprob(model, X_test, sf, X_test_bis=None):

    y_pp_1 = model.predict_proba(X_test)[:, 1] 
    y_pp_0 = model.predict_proba(X_test)[:, 0]

    if type(sf) is tuple:
        if X_test_bis is None:
            raise Exception("X_test_bis should be given.")
        gp0, gp1 = sf
        y_pp_sf1 = y_pp_1[X_test_bis[gp1] == 1]
        y_pp_sf0 = y_pp_0[X_test_bis[gp0] == 0]
    elif type(sf) is str:
        y_pp_sf1 = y_pp_1[X_test[sf] == 1]
        y_pp_sf0 = y_pp_0[X_test[sf] == 0]

    return y_pp_sf0, y_pp_sf1
