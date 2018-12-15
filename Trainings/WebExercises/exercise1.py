import datetime
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

def getting_older():
   name = input('Enter your name ')
   age = input('Enter your age')
   now=datetime.datetime.now()
   print(now.year)
   message = name + 'In ' +  str(now.year+ 100-int(age))
   print(message)
   random_number = input('Please provide any random number')
   for i in range(int(random_number)):
       print(message)

getting_older()

