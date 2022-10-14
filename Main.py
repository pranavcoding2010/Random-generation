import random
number = random.randint(1,20)
playername = print("Hello,whats your name ?")
print("Hi",playername,"Please guess a number between 1 and 20")
numberofguess = 0
while numberofguess<5 :
    guess = int(input())
    numberofguess+=1
    if guess<number:
        print("Your guess is too low")
    elif guess>number:
        print("Your guess is too high")
    elif guess == number:
        break 
if guess == number:
    print("You  have guessed it correctly")
else:
    print("Incorrect guess the correct number is",number)