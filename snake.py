'''
1 for snake 
-1 for water
0 for gun
'''
import random

computer = random.choice([1, -1, 0])
youstr=input("enter your choice:")
dict = {"s" : 1,"w" :-1,"g":0}
reversed_dict = {1:"snake",-1:"water",0:"gun"}

you = dict[youstr]
print(f"you choose {reversed_dict[you]} \n computer choose {reversed_dict[computer]}")
if (computer == you ):
    print("its a draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 1 and you == -1):
        print("you lose")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you lose")
    elif(computer == 0 and you == -1):
        print("you win")
    else:
        print("something went wrong")

