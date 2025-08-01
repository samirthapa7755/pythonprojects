import random
n = random.randint(1,100)
a = -1
guesses = 0


while(a != n):
    a = int(input("enter your guess:"))
    guesses += 1
    if(a>n):
        print("enter lower number")
    elif(a<n):
        print("enter higher number")
        

print(f"you have guessed the number {n} in {guesses} attempts")        