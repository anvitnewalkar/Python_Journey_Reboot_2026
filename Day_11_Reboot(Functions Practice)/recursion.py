# 1. Write a recursive function factorial(n) that returns the factorial of a number

"""def factorial(n):
    if  n == 0 or n == 1:
        return 1 
    return n * factorial(n - 1)
    
n = int(input("enter a number:- "))
print(f"The factorial of n is:- {factorial(n)}")"""



##############################################################################3


# 2. Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.


def sum_of_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)

print(f"Sum of all digits of a number is:-{sum_of_digits(2428)}") 
