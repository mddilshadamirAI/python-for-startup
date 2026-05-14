#Ask user if they are new or old user
Choose = input("Are you new or old user? ")
if Choose == "new":
    print("Welcome")
    name = input("What's your name ?")
    print("Nice to meet you " + name)
    password = input("Please choose a password: ")
    print("Your password has been set")
elif Choose == "old":
    print("Welcome back") 
    password = input("Enter your password")
    name = input("What's your name ?")
    print("Nice to meet you again" + name)
