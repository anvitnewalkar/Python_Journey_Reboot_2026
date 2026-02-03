secret_pass = "242819"

attempt= ""   #You create an empty variable. This is where the user's guess will go. You must create it before the loop so the loop has something to check.

count = 0     #This is your "Strike Counter." It starts at zero because the user hasn't made any mistakes yet.

while attempt != 0 and count < 3:
    attempt = input("Enter Password")
    
    if attempt == secret_pass:
        print("Access Granted")
        break
    
    else:
        print("Try Again")
        count += 1

    if count == 3:
        print("System Locked")
