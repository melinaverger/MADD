"""
Created on: Fri. 5 Aug. 2022
Updated on: Tue. 9 Aug. 2022
Updated on: Wed. 31 Aug. 2022
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



## Start the clock

start_time = time.monotonic()



## Read the data

studentAll = pd.read_csv("./data/studentAll.csv")
print("----------\nRead 'studentInfo.All'.", flush=True)



## Remove missing and noisy values (in the rows)

# Missing values
studentAll = studentAll.dropna(subset=['imd_band']) # from previous studies, we know that there are 1,111 (then 1,030) missing values within this feature

# Noise
studentAll = studentAll[studentAll.final_result != "Withdrawn"]
# kept for the second xp: studentInfo = studentInfo[studentInfo.final_result != "Distinction"]

# Noise (duplicates)
studentAll = studentAll.drop_duplicates(subset=["id_student"], keep="first")
studentAll = studentAll.drop(columns=["id_student"])

print("Missing and noisy values removed.", flush=True)



## Encoding categorical features

studentAll_num = encoding(studentAll)
print("Categorical features encoded.", flush=True)

studentAll_num_columns = studentAll_num.columns
studentAll_num.to_csv("./data/studentAll_num.csv", index=False)
print("Numerical data set saved in 'studentAll_num.csv' file.", flush=True)



## Scale the data (https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data)

studentAll_num_scaled = minmax_scaling(studentAll_num, columns = studentAll_num_columns, min_val=0, max_val=1)



## Save dataframe

studentAll_num_scaled.to_csv("./data/studentAll_num_scaled.csv", index=False)
print("Numerical scaled data set saved in 'studentAll_num_scaled.csv' file.", flush=True)



## End the clock

end_time = time.monotonic()

print("----------\nExecution time:", timedelta(seconds=end_time - start_time), flush=True)