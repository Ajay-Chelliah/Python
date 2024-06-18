import random;
print("Welcome to the game of PIG")
choice = input("Press y to play the game or n to exit ").lower()
total = 0
if(choice == 'y'):
    while(True):
        dice = random.randint(1,6)
        print(f'You got {dice}')
        if(dice!=1):
            total = total + dice
        else:
            total = 0
            print(f'Your total score is {total}')
        if(total==50):
            print("You win!")
        elif(total<50):
            print(f'Your score is {total}')
        else:
            print("You already won the game")
            exit()
        opt = input("Do you want to continue the game if yes press y or any key ").lower()
        if(opt !='y'):
            break
elif(choice == 'n'):
    exit()
else:
    print("You entered the wrong letter")