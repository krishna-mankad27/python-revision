import random
import emoji
lnum = 1
hnum = 10
ans = random.randint(lnum,hnum)
guesses = 0
while True: 
    guess = input(f"enter your guess between {lnum} and {hnum} :")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if lnum <= guess <= hnum :
            if guess == ans:
                print(emoji.emojize("HURRAYYY YOU WON:party_popper::party_popper::party_popper::party_popper:"))
                print(f"In {guesses} guesses ")
                break
            elif guess < ans:
                print("your guess is smaller than answer")
            else:
                print("your guess is greater than answer")
        else:
            print("invalid input....\nOut of Range\n--------------------")
    else:
        print("invalid input....\n--------------------")