from random import *

'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
for x in range(10):
  print random.randint(1,101)
  
  Extras:

Keep the game going until the user types “exit”

Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''



def ran():

 count_guess_nr=0

 while True:
   random_number = input("Enter random number from 1 to 9 ")
   count_guess_nr=count_guess_nr+1

   # Keep the game going until the user types “exit”
   if (str(random_number) == "exit"):
       break

   random_number_converted = float(random_number)
   generated_number = randint(1, 10)

   if (random_number_converted==generated_number):
    print("You guessed")
    break

   elif (random_number_converted < generated_number):
    print ("your number is too small keep on guessing")
    continue

   elif (random_number_converted > generated_number):
    print ("your number is too big keep on guessing")
    continue
 print("Number of user guesses" + str(count_guess_nr))

ran()