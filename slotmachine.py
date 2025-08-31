import random
import time
def spinrow(l1):
    x = random.choice(l1)
    return x
def printrow(r):
    for i in r:
        print(i,end = " ")
def payout(n,l):
    if l[0] == l[1] and l[1] == l[2]:
        print("******JACKPOT******")
        n = n*5
    elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
        print("you won!!!")
        n = n*2
    else :
        n = -n
        print("YOU LOST ")
    return n
def main():
    print("**********WELCOME**********")
    print("symbols : 😊😂🤣❤️😍😁")
    symbols = ["😊","😂","🤣","❤️","😍","😁"]
    row = []
    round = 1
    balance = int(input("Enter amount : "))
    while True:
        if balance <= 0:
            print("insufficient funds")
            c = True
            while c:
                choice = input("2. ADD MONEY \n3. Quit\n=> ")    
                if choice == "1": 
                    print("enter 2 or 3")
                else :
                    c = False 
        else:
            choice = input("1. Play\n2. ADD MONEY \n3. Quit\n=> ")    
        match choice:
            case "1":
                row = []
                print(f"------ROUND:{round}--------")
                bet = int(input("How much do you want to bet : "))
                if bet > balance:
                    print("insufficient funds")
                    continue
                print("spinning.....")
                time.sleep(3)
                for i in range(3):
                    row.append(spinrow(symbols))
                printrow(row)
                balance += payout(bet,row)
                print(f"Your prize : {balance}")
                round += 1
            case "2":
                balance += int(input("Enter amount : "))
                print(f"Your balance : {balance}")
            case "3":
                print(f"Your prize : {balance}")
                print("thanks for playing")
                break
            case _ :
                print("please select a valid choice")

if __name__ == "__main__":
    main()