import random
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

def list_comparision():
    list1= input('enter first list')
    list2= input('enter second list')
    list3=[]
    print(list1)
    print(list2)

    #for each element in List A and for each element in ListB, if A is different than B and unique in C add to C

    for a in list1:
        for b in list2:
            if (a ==b):
                if a not in list3:
                    list3.append(a)
    print(list3)

list_comparision()
