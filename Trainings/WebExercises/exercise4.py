'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def number_divisor():

    #ask for a number
    number=int(input("Enter number "))
    list=[]

    #print out list of all the divisors of that number

    for i in range(1, number+1):
        if (number %i) == 0:
            list.append(i)
            print("found divisor" + str(i))
    return print(list)

number_divisor()
