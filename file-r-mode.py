#                        R-MODE
#--------------------------------------------------------

import json
import csv

# -------------------------txt file----------------------
# emp = ["hehe","haha","hoho","hihi"]
# try:
#     with open(file = "C:\\Users\\krishna\\Desktop\\hey\\output.txt",mode = "r") as file:
#         content = file.read()
#         print(content)
# except FileExistsError:
#     print("that file already exists")
# except PermissionError:
#     print("file locked")
# -------------------------------------------------------
# ------------------------json file----------------------
# try:
#     with open(file = "c:\\Users\\krishna\\Desktop\\hey\\output.json",mode = "r") as file:
#         content = json.load(file)
#         print(content["name"])
# except FileNotFoundError:
#     print("file not found")
# -------------------------------------------------------
# ------------------------csv file-----------------------
try:
    with open(file = "c:\\Users\\krishna\\Desktop\\hey\\output.csv",mode = "r") as file:
        content = csv.reader(file)
        for i in content:
            for j in range (3):
                print(i[j],end = " ")
            print("")
except FileNotFoundError:
    print("file not found")