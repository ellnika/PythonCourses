'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

def new_list():
    old_list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    #old_list=list(input('Enter your list '))
    new_list=[]
    #iterate through list

    for i in old_list:
        if i %2 ==0:
            new_list.append(i)
    print(new_list)

new_list()