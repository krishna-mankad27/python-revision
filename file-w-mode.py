import os
import json
import csv
# 

#                         W-MODE



# 
# f = "C:/Users/krishna/Desktop/hey"
# if os.path.exists(f):
#     print("file exists")
# if os.path.isfile(f):
#     print("is file")
# if os.path.isdir(f):
#     print("this is dir")
# else:
#     print("file doesnt exist")
f = "hello world"
fp = "output.txt"

# -----------------------------txt file--------------------------
# emp = ["hehe","haha","hoho","hihi"]
# try:
#     with open(file = "C:/Users/krishna/Desktop/hey/output.txt",mode = "a") as file:
#         for i in emp:
#             file.write("\n"+i)
#         print(f"txt file{fp} was created")
# except FileExistsError:
#     print("that file already exists")
#----------------------------------------------------------------
#------------------------------json file-------------------------
# emp = {"name" : "hihi","age" : "34","gender": "fimail","job": "cook"}
# try:
#     with open(file = "C:/Users/krishna/Desktop/hey/output.json",mode = "w") as file:
#         json.dump(emp,file,indent="")
#         print(f"json file{fp} was created")
# except FileExistsError:
#     print("that file already exists")
#----------------------------------------------------------------
#-------------------------------csv file-------------------------
emp = [["name","age","gender"],["krishna",20,"male"],["tillu",19,"male"],["randi",20,"chakka"]]
try:
    with open(file = "C:/Users/krishna/Desktop/hey/output.csv",mode = "w",newline="") as file:
        writer = csv.writer(file)
        for i in emp:
            writer.writerow(i)
        print(f"csv file{fp} was created")
except FileExistsError:
    print("that file already exists")
