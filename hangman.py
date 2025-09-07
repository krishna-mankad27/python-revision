import random
key = ["apple","banana","mango","kiwi","lichi"]
hangman =  {0: ("   ",
                "   ",
                "   "),
            1: (" o ",
                "   ",
                "   "),
            2: (" o ",
                " | ",
                "   "),
            3: (" o ",
                "/| ",
                "   "),
            4: (" o ",
                "/|\\",
                "   "),
            5: (" o ",
                "/|\\",
                "/  "),
            6: (" o ",
                "/|\\",
                "/ \\")}
def display(n):
    for i in hangman[n]:
        print(i)

    
def main():
    c = 0
    answer = random.choice(key)
    y = len(answer)
    user = ["_"]*y
    print(user)
    won = False
    
    guessed = []
    while c < 6:
        correct = False
        guess = input("enter guess : ").lower()
        if guess.isdigit() or not guess.isalpha():
            print("INVALID INPUT...")
        elif guess in guessed:
            print("ALREADY GUESSED...")
            continue
        else:
            guessed.append(guess)
            for i in range(y):
                if answer[i] == guess:
                    user[i] = guess
                    correct= True
            print(user)
        if "_" not in user:
            print("YOU WON...")
            won  = True
            display(c)
            break
        if not correct:
            c+=1
        display(c)
    if not won:
        print("YOU LOST...") 
main()