#import and generate random integer between 1 and 100
#assign it to variable ran
import random
ran = random.randint(1, 100)

print("This is not my black belt.  Please actually choose a number")
print("     ")

#probably is already but make it an integer just in case
int(ran)

#display start menu with input prompt
#describe game
input("To play the game      NumberGuess      press enter")
print("Try to guess the secret number between 1 and 100")
print("You have 7 tries")

#make my stop mechanism
stop = False

#get input assign as first guess
gs1 = int(input("Try to guess."))

#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
if gs1 == ran:
    print("Congratulations")
    print("Rank = Felix Felicis")
    #obscure Harry Potter reference
    print("Number of guesses needed = 1")
    stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs1 > ran:
        print("Too high")
    if gs1 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number
if stop == False:
    gs2 = int(input("Try to guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs2 == ran:
        print("Congratulations")
        print("Number of guesses needed = 2")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("The oracle was right, your are the 1")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs2 > ran:
        print("Too high")
    if gs2 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number
   
if stop == False:
    gs3 = int(input("Try to guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs3 == ran:
        print("Congratulations. 3 tries! Amazing")
        print("Rank = Jedi Master")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("Number of guesses needed = 3")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs3 > ran:
        print("Too high")
    if gs3 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number

if stop == False:
    gs4 = int(input("Try to guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs4 == ran:
        print("Congratulations")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("Perhaps the Oracle was right, you may be the 1")
        print("Number of guesses needed = 4")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs4 > ran:
        print("Too high")
    if gs4 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number

if stop == False:
    gs5 = int(input("Try to guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs5 == ran:
        print("Congratulations.")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("Strong in you, the Force is.")
        print("Rank = Jedi")
        print("Number of guesses needed = 5")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs5 > ran:
        print("Too high")
    if gs5 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number
        
if stop == False:
    gs6 = int(input("Try to guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs6 == ran:
        print("Congratulations.")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("Rank = Young Padawan")
        print("Number of guesses needed = 6")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low

if stop == False:
    if gs6 > ran:
        print("Too high")
    if gs6 < ran:
        print("Too low")

#if stop is still false get another guess as input from user
#assign that input to the gs number

if stop == False:
    gs7 = int(input("Last guess."))
#if guess equals ran then make stop true
#tell the user they won
#and display number of guesses
    if gs7 == ran:
        print("Congratulations")
        #make the program enjoyable to your stereotypical programmer :)
        #do this by scifi references
        #i.e. the matrix, star wars and Harry Potter
        print("Rank =  Muggle")
        #7 is not special, sorry
        print("Number of guesses needed = 7")
        stop = True

#continue only if stop is false, this means they have not got it right, yet
#if guess is more than value of ran print too high
#if guess is less than value of ran print too low
#inform the user that they are not special

if stop == False:
    if gs7 > ran:
        print("Too high")
        #matrix reference
        print("I am sorry you are not the 1")
        print("Rank = Mountain Troll")
        print("Game Over")
        
    if gs7 < ran:
        print("Too low")
        #matrix reference
        print("Perhaps the prophecy is not about you.")
        print("You are not the 1")
        print("Rank = Garden Gnome")
        print("Game Over")





