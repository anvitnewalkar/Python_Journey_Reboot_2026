# 0  1  1  2  3  5  8  13  21
 
# 0  1  2  3  4  5  6  7   8



"""def fib(n):
    if n == 0 or n == 1:
        return n 
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(6))
print(fib(7))"""


def factorial(n):
    if n == 0 or n == 1:       # Base case.....
         return 1
    
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter number:-"))

print(f"The factorial of entered number is:-{factorial(n)}")   # Calling Function....