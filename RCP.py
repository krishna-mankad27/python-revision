#rock paper scissors 
import emoji
import random
hand = ["rock","paper","scissors"]
uscore = 0
aiscore = 0
round = 1
while True:
    print(f"        round : {round}")
    ai = random.choice(hand)
    print(ai)
    user = input("Enter a choice [rock,paper,scissors] \nEnter q to quit\n=>")
    if user in hand :
        round += 1
        if ai == "rock":
            if user == "paper":
                uscore += 1
                print(emoji.emojize("HURRAYYY YOU WON:party_popper::party_popper::party_popper::party_popper:"))
            elif user == ai:
                print("TIE...")
            else:
                aiscore += 1
                print("YOU LOST....")

        elif ai == "paper":
            if user == "scissors":
                uscore += 1
                print(emoji.emojize("HURRAYYY YOU WON:party_popper::party_popper::party_popper::party_popper:"))
            elif user == ai:
                print("TIE...")
            else:
                aiscore += 1
                print("YOU LOST....")
        elif ai == "scissors":
            if user == "rock":
                uscore += 1
                print(emoji.emojize("HURRAYYY YOU WON:party_popper::party_popper::party_popper::party_popper:"))
            elif user == ai:
                print("TIE...")
            else:
                aiscore += 1
                print("YOU LOST....")
    elif user == "q":
        print("---------------------------")
        print(f"SCORE : user = {uscore}\n        ai   = {aiscore}")
        print("thanks for playing ")
        print("---------------------------")
        break
    else:
        print(f"INVALID INPUT \nPlease choose from {hand} : ")
    print("---------------------------") 