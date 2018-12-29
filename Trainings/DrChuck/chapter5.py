'''
Write a program that repeatedly reads numbers until user enters "done".
Once done is entered, print total, everage and count of the numbers.
If user enters anything else than a number, detect their mistake using try and except and print an error message
and skip to next number

accumulate pattern
counter pattern

'''

# iteration variable for count
#

def test():

    count = 0
    total = 0.0

    while True:

      svar = input("Enter a number ")
      if (svar) == "done" : break

      try:
       fvar  = float(svar)

      except:
        print("Invalid Input")
        continue

      count = count + 1
      total = total + fvar

    print ("ALL DONE")
    print (count)
    print(total)
    print(total/count)

#test()

'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.

'''


def exercise7():

    biggest = 0
    smallest = None
    count = 0

    while True:
      user_input=input("Enter integer number ")
      if (user_input) == "done":
          print("biggest number is " + str(biggest))
          print("smallest number is " + str(smallest))
          break
      try: user_input_int= int(user_input)
      except :
        print("Invalid input")
        continue

      if biggest is None or user_input_int > biggest:
        biggest = user_input_int
      if smallest is None or user_input_int < smallest:
        smallest = user_input_int


exercise7()

'''
Write a program that counts down from five and then says "Blasoff"
'''

def countdown():
 count = 5
 while count >=0:
    print(count)
    count = count - 1

#countdown()