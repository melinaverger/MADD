"""
Created on: Fri. 5 Aug. 2022
Updated on: Tue. 9 Aug. 2022
Author: Mélina Verger
"""

## Libraries

# To check the execution time of the script
import time
from datetime import timedelta

# For data maniuplation and analysis
import pandas as pd

# For encoding
from encode_features import encoding

# To scale the data
from mlxtend.preprocessing import minmax_scaling

# Plotting modules
import seaborn as sns
import matplotlib.pyplot as plt



## Start the clock

start_time = time.monotonic()



## Read the data

studentInfo = pd.read_csv("./data/studentInfo.csv")
print("----------\nRead 'studentInfo.csv'.", flush=True)



## Remove missing and noisy values (in the rows)

# Missing values
studentInfo = studentInfo.dropna(subset=['imd_band']) # from previous studies, we know that there are 1,111 missing values within this feature

# Noise
studentInfo = studentInfo[studentInfo.final_result != "Withdrawn"]
studentInfo = studentInfo[studentInfo.final_result != "Distinction"]

# Noise (duplicates)
studentInfo = studentInfo.drop_duplicates(subset=["id_student"], keep="first")
studentInfo = studentInfo.drop(columns=["id_student"])

print("Missing and noisy values removed.", flush=True)



## Encoding categorical features

studentInfo_num = encoding(studentInfo)
print("Categorical features encoded.", flush=True)

studentInfo_num_columns = studentInfo_num.columns
studentInfo_num.to_csv("./data/studentInfo_num.csv", index=False)
print("Numerical data set saved in 'studentInfo_num.csv' file.", flush=True)



## Scale the data (https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data)

studentInfo_num_scaled = minmax_scaling(studentInfo_num, columns = studentInfo_num_columns, min_val=0, max_val=1)



## Save dataframe

studentInfo_num_scaled.to_csv("./data/studentInfo_num_scaled.csv", index=False)
print("Numerical scaled data set saved in 'studentInfo_num_scaled.csv' file.", flush=True)



## End the clock

end_time = time.monotonic()

print("----------\nExecution time:", timedelta(seconds=end_time - start_time), flush=True)