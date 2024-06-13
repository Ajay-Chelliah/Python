import random;
print("Welcome to NUMBER GUESSING game")
willing = input("Do you want to play?")
if(willing.lower() != "yes"):
    exit()
print("lets begin")
i=1
score=0
while(i!=0):
    guess = int(input("Guess a number between 0 and 11"))
    num = random.randint(0,11)
    if(guess == num):
        print("Your guess is correct")
        score=score+1
    else:
        print(num)
        print("Your guess is wrong")
    i = int(input("If you want to end the game enter 0 or 1"))
