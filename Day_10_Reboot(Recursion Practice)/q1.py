# Write a program using functions to find greatest of three numbers. 

def greatest(a, b, c):
    if (a > b and a > c):
        return a
    
    elif (b > a and b > c):
        return b

    elif (c > a and c > b):
       return c

    else:
        return f"Nothing Happened"


a = 10
b = 204
c = 30

print(greatest(a, b, c))


# In 1st attempt I have made a small logic mistake. I have written or logic instead of and. 