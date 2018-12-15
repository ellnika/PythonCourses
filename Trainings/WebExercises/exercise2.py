'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def odd_even():
    number_one=int(input('Please enter any number '))

    if number_one % 2 == 0:
        print('The number you entered is even')

        if number_one % 4 == 0:
            print('the number is multiply of 4')
    else:
        print('The number you entered is odd')

#odd_even()

def number_check():
    num=int(input('Enter first number '))
    check=int(input('Enter second number'))
    if check%num == 0:
        print('first number dives by second')
    else:
        print('first number does not divide by second')

number_check()

