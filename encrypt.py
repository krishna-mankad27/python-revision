import random
import string
f = string.ascii_letters + string.punctuation + string.digits + " "
key =list(f)
f = key.copy()
random.shuffle(key)
print(f,"\n",key)
# text = input("enter text to be encrypted : ")
# code = ""
#encryption
while True:
    x = input("enter choice : ")
    if x == "1":   
        text = input("enter text to be encrypted : ")
        code = ""
        for i in text:
            index  = f.index(i)
            code = code + key[index]
        print("encrypted message : ", code)
    elif x == "2":
        #decryption
        message =""
        y = input("enter message : ")
        for i in y:
            index = key.index(i)
            message = message + f[index]
        print(message)
    else :
        break