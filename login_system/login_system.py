username = input("Enter username")

password = input("Enter password")

if username == "admin":
    
    if password == "1234":

        print("Welcome Master")

    else:
        print("Incorrect Password")

else:
    print("User not found!")