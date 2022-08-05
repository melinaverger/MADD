"""
Created on: Fri. 5 Aug. 2022
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
from sklearn.preprocessing import StandardScaler



## Start the clock

start_time = time.monotonic()



## Read the data

studentInfo = pd.read_csv("./data/studentInfo.csv")
print("----------\nRead 'studentInfo.csv'.", flush=True)



## Remove missing and noisy values

studentInfo = studentInfo.dropna(subset=['imd_band']) # from previous studies, we know that there are 1111 missing values within this feature

studentInfo = studentInfo[studentInfo.final_result != "Withdrawn"]
studentInfo = studentInfo[studentInfo.final_result != "Distinction"]

print("Missing and noisy values removed.", flush=True)



## Encoding categorical features

studentInfo_num = encoding(studentInfo)



# Scale the data

scaler = StandardScaler()
scaler.fit(studentInfo_num)
studentInfo_num = scaler.transform(studentInfo_num)



## Save dataframe

studentInfo_num.to_csv("./data/studentInfo_num.csv", index=False)
print("Save numerical data set.", flush=True)



## End the clock

end_time = time.monotonic()

print("----------\nExecution time:", timedelta(seconds=end_time - start_time), flush=True)