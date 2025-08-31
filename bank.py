#banking program 
b = 00.00
def balance():
    global b
    print(f"Your balance  = {b}")
def withdraw():
    global b
    y = float(input("Enter amount to be withdrawn : "))
    if b > y and y > 0:
        b -= y
        print(f"Remaining balance = {b}")
    elif b < y:
        print("Not enough balance")
    elif y <= 0 :
        print("INVALID AMOUNT")
def deposit():
    global b
    x = float(input("Enter amount to be deposited : "))
    if x <= 0 :
        print("INVALID AMOUNT")
    else:
        b += x
        print(f"Current balance = {b}")
print("------------Banking Program------------")
while True:
    print("1. Show balance\n2. Deposit Money\n3. Withdraw Money\n4. Quit Program")
    choice = input("Enter your choice : ")
    print("---------------------------------------")
    match choice:
        case "1":
            balance()
        case "2":
            deposit()
        case "3":
            withdraw()
        case "4":
            break
        case _ :
            print("please enter a valid choice")
    print("---------------------------------------")
print("-------PROGRAM ENDED SUCCESFULLY--------")