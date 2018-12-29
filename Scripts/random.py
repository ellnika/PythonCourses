loose="Computer wins"
win="You win"
lives = 5
score = 0
computer_lives = 7
while True:
    print("To begin fil in the below information: ")
    username=input("Please enter your username: ")
    password = input("Please enter your password ")
    searchfile = open("accounts.cvs", "r")
    for line in searchfile:
        if username and password in line:
            print("access granted ")