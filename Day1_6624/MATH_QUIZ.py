import random
import time
operators = ['+','-','*']
while(True):
    choice = input("Do you want the level of the game to be easy,medium and difficult ")
    if(choice == 'easy'):
        min,max = 3,11
        break
    elif(choice == 'medium'):
        min,max = 100,1000
        break
    elif(choice == 'hard'):
        min,max = 998,999999
        break
    else:
        print("Enter a correct choice")
print("--------------------------------")
count = 3
point = 0
def generate(): 
    num1 = random.randint(min,max)
    num2 = random.randint(min,max)
    operator = random.choice(operators)
    expr = (str)(num1) +  operator + (str)(num2)
    result = eval(expr)
    return expr,result
start = input("ready to start the game press y ").lower()
if(start!='y'):
    exit()
start_time = time.time()
for i in range(1,count+1):
    expr,result = generate()
    guess= input(f'Enter the result {expr} ')
    if(guess==(str)(result)):
        print("you are correct")
        point = point+1
end_time = time.time()
print(point)
print(end_time - start_time)