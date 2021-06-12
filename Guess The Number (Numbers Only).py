from random import *
Random_Value = randint(1,100)
Guess = float(input("This is the 'Guess the number' game. I'm thinking of a number between 1 and 100. \n" 
      "If you guess right, you'll get a cookie. \n" "If not, I'll tell you whether your guess is too high or too low and you can guess again. \n"
       "What's your first guess? \n"))

while Guess != Random_Value:
    if Guess % 2 != 0 and Guess % 2 != 1:
        Guess = round(Guess)
        print("We're only going to use integers for this game so let's make that", Guess)
    if Guess > Random_Value:
        Guess = float(input("Your guess is too high. Let's try again \n"))
    else:
        Guess = float(input("Your guess is too low. Let's try again \n"))
        
if Guess == Random_Value:
    print("Hurray! Here's your cookie")