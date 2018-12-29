'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Michele
Then I would see the string:

Michele is name My
shown back to me.
'''

def print_backwards():
    user_input=input("enter string ")
    user_input_list=user_input.split()
    print(user_input_list.reverse())



print_backwards()

#iterate through list

#print last element of list as first

#convert string to list

