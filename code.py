###Made By Oplikoo(Oplikoo/Python-Random-Number)
###Have Any Errors? Fill free to contact me on the github page
###Have fun with the code!
###--------------------------------------------------------------

#Imports the random library
import random
print("Ok, I loaded The code!")
#its random a number between 1 to 10
randomnum = random.randint(1,10)
#Gets the guess that the user typed. Its also convert it to a number so if its not a number the code will stop
guess = int(input("Guess The number between 1 to 10! Your Guess : "))
#if the guess that the user typed is correct
if(guess == randomnum):
        print("Congrats, You Won the game!")
#if the guess is wrong and the bot randomed another number
else:
        print("Sorry, But you lose the game! The number I chose is  " , randomnum , ", And not your guess, That was " , guess , ".")
#And yes that is all the code...
#Not so hard to edit or view
#Like this project? A star in this github project will be amazing(and also will support me to make more github projects)!
