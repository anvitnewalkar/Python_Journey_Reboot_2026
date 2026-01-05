a = int(input("Enter a number between 1 and 10:"))

match a:
    case 1:
        print("You have won a charger.")
    
    case 3:
        print("You have won $3.")
    
    case 6:
        print("You have won a camera.")

    case _:
        print("Better luck next time.")