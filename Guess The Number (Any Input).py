from random import *


###------------Generate a random value between 1 and 100------------###
Random_Value = randint(1,100)



###------------User's input------------###
Guess = input("This is the 'Guess the number' game. I'm thinking of a number between 1 and 100. \n" 
      "If you guess right, you'll get a cookie. \n" "If not, I'll tell you whether your guess is too high or too low and you can guess again. \n"
       "What's your first guess? \n")



###------------Create a list where each word of the user's input is split into an element------------###
Scan_Guess = Guess.split()



###------------Tests wether a given string is a number------------###
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False



###------------Tests wether a given number has decimals------------###
def Decimal_check():
    global Guess
    if Guess % 2 != 0 and Guess % 2 != 1:
        return True
    else:
        return False
            


###------------Tests wether user's given number (if any is found) is equal to the randomly generated number------------###
def Equality_check():
    global Guess
    if Guess != Random_Value:
        if Guess > Random_Value:
            Guess = input("Your guess is too high. Let's try again \n")
        else:
            Guess = input("Your guess is too low. Let's try again \n")
    return



###------------Create infinite loop that restarts every time different input is given------------###
restart = True
while restart:
    for i in range(len(Scan_Guess)):
        Guess = Scan_Guess[i]
        if is_number(Guess):
            Guess = float(Scan_Guess[i])
            if Decimal_check():
                Guess = round(Guess)
                print("We're only going to use integers for this game so let's make that", Guess)
            Equality_check()
            Scan_Guess = str(Guess).split()
            i = 0
        else:
            if i == len(Scan_Guess)-1 and is_number(Guess) is False:
                Scan_Guess = input("I'm sorry, I can only accept numbers. Let's try that again. \n").split()
                Guess = Scan_Guess
        if Guess == Random_Value:
            print("Hurray! Here's your cookie")
            restart = False                   ### breaks the loop if numbers are equal