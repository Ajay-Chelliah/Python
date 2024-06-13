import random
list1 = ['rock','paper','scissors']
choice = random.choice(list1).lower()
guess = input("Enter your guess").lower()
if(choice == guess):
    print(choice)
    print("The game is draw")
elif(guess == "rock"):
    if(choice == "scissors"):
        print(choice)
        print("you win")
    else:
        print(choice)
        print("you lose")
elif(guess == "paper"):
    if(choice == "scissors"):
        print(choice)
        print("you lose")
    else:
        print(choice)
        print("you win")
elif(guess == "scissors"):
    if(choice == "paper"):
        print(choice)
        print("you win")
    else:
        print(choice)
        print("you lose")