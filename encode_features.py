"""
Created on: Fri. 5 Aug. 2022
Updated on: Tue. 9 Aug. 2022
Author: Mélina Verger
"""

## Libraries

# For data maniuplation
import pandas as pd



## Encoding categorical features

# Label encoding (order)

def encode_gender(x):
    if x == 'M':
        return 1
    else:
        return 0

def encode_education(x):
    if x == "No Formal quals":
        return 0
    elif x == "Lower Than A Level":
        return 1
    elif x == "A Level or Equivalent":
        return 2
    elif x == "HE Qualification":
        return 3
    else:  # "Post Graduate Qualification"
        return 4

def encode_imd(x):
    if x in ['0-10%', '10-20', '20-30%', '30-40%', '40-50%']:
        return 1
    elif x in ['50-60%', '60-70%', '70-80%', '80-90%', '90-100%']:
        return 0
    else:
        raise ValueError("Missing values should have been removed.")

def encode_age(x):
    if x == "0-35":
        return 0
    elif x == "35-55":
        return 1
    else:  # "55<="
        return 2

def encode_disability(x):
    if x == "Y":
        return 1
    else:  # "N"
        return 0

def encode_final_result(x):
    if x == "Pass":
        return 1
    else:  # "Fail"
        return 0

def labelencoding(dataframe):
    # specific syntax to avoid SettingWithCopyWarning
    dataframe.loc[:, "gender"] = dataframe.gender.apply(encode_gender)
    dataframe.loc[:, 'highest_education'] = dataframe.highest_education.apply(encode_education)
    dataframe.loc[:, 'imd_band'] = dataframe.imd_band.apply(encode_imd)
    dataframe.loc[:, 'age_band'] = dataframe.age_band.apply(encode_age)
    dataframe.loc[:, 'disability'] = dataframe.disability.apply(encode_disability)
    dataframe.loc[:, 'final_result'] = dataframe.final_result.apply(encode_final_result)
    return dataframe

# One-hot encoding

def onehotencoding(dataframe):
    # prevent from feature removing before encoding
    col = list()
    for column in dataframe.columns:
        if column == "code_module" or column == "code_presentation" or column == "region":
            col.append(column)

    return pd.get_dummies(dataframe, columns=col)

# Encoding

def encoding(dataframe):
    dataframe = onehotencoding(dataframe)
    dataframe = labelencoding(dataframe)
    return dataframe
