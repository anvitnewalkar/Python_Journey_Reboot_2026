# 1. Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across functioncalls.


"""def increment():
    counter = 0
    counter += 1
    print(counter)

increment()"""



#########################################################################################


# 2. Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''
    Multiply two numbers

    Parameters:
        a = (int or float): The first number.
        b = (int or float): The second number.

    Returns:
       int or float: The product of a and b. 
    
    '''

    return a * b

# Example

print(f"The multiplication of a and b is:- {multiply(5, 3)}")
print(f"The multiplication of a and b is:- {multiply(5.2, 3)}")

help(multiply)
