#keep asking for input when it is invalid 
#username must not contain digits
#username must be less than or equal to 12 characters
#username must not contain spaces
isvalid = False
while isvalid == False :
    name  = input("enter username : ")
    space = name.find(' ')
    if space == -1:
        x = len(name)
        if x <= 12:
            space = name.find(' ')
            if name.isalpha() == True:
                isvalid = True
                print("username valid...")
            else:
                print("invalid username ...\nusername cannot contain digits")
        else:
            print("invalid username ...\nusername cannot contain more than 12 characters")        
    else:
        print("invalid username ...\nusername cannot contain spaces")
