"""
Created on: Fri. 5 Aug. 2022
Author: Mélina Verger
"""

## Libraries

# To interact with the operating system
import os

# To check the execution time of the script
import time
from datetime import timedelta

# To make HTTP requests
import requests

# To interact with ZIP file
import zipfile



## Start the clock

start_time = time.monotonic()



## Assign a constant variable

FILE_NAME = "studentInfo.csv"



## Create and go to a new folder

os.mkdir("data")
print("----------\nCreation of a new folder 'data'.", flush=True)

os.chdir("data")



## Dowload the data from its URL and save the data into a ZIP file

url_data = "https://analyse.kmi.open.ac.uk/open_dataset/download"

response = requests.get(url_data)

open("data.zip", "wb").write(response.content)
print("Data downloaded in the 'data' folder.", flush=True)



## Open the ZIP file and extract one data set

# ZIP file handler
zf = zipfile.ZipFile("data.zip")

# Extract the file from the ZIP folder
zf.extract(FILE_NAME)
print("'" + FILE_NAME + "' extracted into the 'data' folder.", flush=True)



## End the clock

end_time = time.monotonic()

print("----------\nExecution time:", timedelta(seconds=end_time - start_time), flush=True)
