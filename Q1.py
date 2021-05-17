import random
# Gather the user's name and store as varible
MyName= input("Hello! What is your name?") 
number = random.randint(1, 10)
# Display name and greet to user
print ( "Hello, "  + MyName +  " I'm thinking of a number between 1 and 10?")
guess = int(input("Take a guess:"))


if  guess == 7:
    print ("You Win!")
else:print ("You Lose!")