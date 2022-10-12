"""
Created on: Fri. 5 Aug. 2022
Updated on: Tue. 9 Aug. 2022
Updated on: Wed. 31 Aug. 2022
Updated on: Fri. 30 Sep. 2022
Updated on: Wed. 12 Oct. 2022
Author: Mélina Verger

Choose the set, clean missing and noisy values, remove duplicates and 'id_student' column, 
encode categorical features, scale data, and save the prepared set.
"""

## Libraries

# To exit script
from sys import exit

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



## Make the data sets choice and read the data

print("\n----------", flush=True)
user_response1 = input("Do you want to work with stInfo or stAll set? (Write either stInfo or stAll and press enter.)\n> ")
if user_response1 == "stInfo":
    data = pd.read_csv("./data/studentInfo.csv")
    print("Read 'studentInfo.csv'.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
elif user_response1 == "stAll":
    data = pd.read_csv("./data/studentAll.csv")
    print("Read 'studentAll.csv'.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
else:
    print("Invalid choice.")
    exit()



## Remove missing and noisy values (in the rows)

# Missing values
user_response2 = input("\nDo you want to remove missing values from 'imd_band' column? (y/n)\n> ")
if user_response2 == 'y':
    data = data.dropna(subset=['imd_band']) # from previous studies, we know that there are 1,111 (then 1,030) missing values within this feature
    print("Missing values from 'imd_band' removed.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
elif user_response2 == 'n':
    print("Missing values not removed.", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()

# Noise
user_response3 = input("\nDo you want to remove noisy values 'Withdrawn'? (y/n)\n> ")
if user_response3 == 'y':
    data = data[data.final_result != "Withdrawn"]
    print("'Withdrawn' values removed.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
elif user_response3 == 'n':
    print("'Withdrawn' values not removed.", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()

user_response4 = input("\nDo you want to remove noisy values 'Distinction'? (y/n)\n> ")
if user_response4 == 'y':
    data = data[data.final_result != "Distinction"]
    print("'Distinction' values removed.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
elif user_response4 == 'n':
    print("'Distinction' values not removed.", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()

# Noise (duplicates)
user_response5 = input("\nDo you want to remove duplicates of student ids and then remove 'id_student' column? (y/n)\n> ")
if user_response5 == 'y':
    data = data.drop_duplicates(subset=["id_student"], keep="first")
    data = data.drop(columns=["id_student"])
    print("Duplicates and 'id_student' removed.", flush=True)
    print(f"Data shape: {data.shape}", flush=True)
elif user_response5 == 'n':
    print("Duplicates and 'id_student' not removed.", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()

print("\nThe 'missing and noisy values removal' part is over.", flush=True)
print(f"Data shape: {data.shape}\n", flush=True)



## Encoding categorical features

data_num = encoding(data)
print("Categorical features encoded.", flush=True)
print(f"Data shape: {data_num.shape}\n", flush=True)

data_num_columns = data_num.columns
if user_response1 == "stInfo":
    data_num.to_csv("./data/studentInfo_num.csv", index=False)
    print("Numerical data set saved in 'studentInfo_num.csv' file.\n", flush=True)
elif user_response1 == "stAll":
    data_num.to_csv("./data/studentAll_num.csv", index=False)
    print("Numerical data set saved in 'studentAll_num.csv' file.\n", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()


## Scale the data (https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data)

data_num_scaled = minmax_scaling(data_num, columns=data_num_columns, min_val=0, max_val=1)



## Save dataframe

if user_response1 == "stInfo":
    data_num_scaled.to_csv("./data/studentInfo_num_scaled.csv", index=False)
    print("Numerical scaled data set saved in 'studentInfo_num_scaled.csv' file.", flush=True)
elif user_response1 == "stAll":
    data_num_scaled.to_csv("./data/studentAll_num_scaled.csv", index=False)
    print("Numerical scaled data set saved in 'studentAll_num_scaled.csv' file.", flush=True)
else:
    print("Invalid choice.", flush=True)
    exit()


## End the clock

end_time = time.monotonic()

print("----------\nExecution time:", timedelta(seconds=end_time - start_time), flush=True)
print("\n", flush=True)
