# """
# Created on: Mon. 29 Aug. 2022
# Author: Mélina Verger
# """

# ## Libraries

# # To interact with the operating system
# import os

# # To handle ZIP file
# import zipfile



# ## Assign a list variable

# FILE_NAMES = ["studentInfo.csv", "studentAssessment.csv", "studentVle.csv"]



# ## Open the ZIP file and extract one data set

# os.chdir("data")

# # ZIP file handler
# zf = zipfile.ZipFile("data.zip")

# print("----------", flush=True)

# for file_name in FILE_NAMES:
#     if not os.path.exists(file_name):
#         if file_name == "studentVle.csv":  # zip because too heavy
#             # Extract the file from the ZIP folder
#             zf.extract(file_name)
#             open(file_name + ".zip", 'w').write(file_name)
#             os.remove(file_name)
#         else:
#             # Extract the file from the ZIP folder
#             zf.extract(file_name)
#         print("'" + file_name + "' extracted into the 'data' folder.", flush=True)
#     else:
#         print("'.data/" + file_name + "' already exists.", flush=True)

# print("----------\n", flush=True)
