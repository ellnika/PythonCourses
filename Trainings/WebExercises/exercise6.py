'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

madam or racecar or the number 10201."
the empty string is a palindrome;
a string constituted only by a single character is a palindrome;

# Loop over string indexes.
for i in range(0, len(s)):
    print(s[i])
'''

def is_palindrome():
    user_input=input('Enter any string ')
    list=[]

    if (len(user_input)<=1):
        print("Input less than 1 digit or one character")
        return 1
    else:
         for i in range(0, len(user_input)):
            if user_input[i] == (user_input[len(user_input)-1-i]):
                list.append(user_input[i])
    list = ''.join(list)
    print(list)
    if (user_input==list):
        print(user_input+ " is palindrome")
    else:
        print(user_input+ "is not plaindrome")

is_palindrome()
