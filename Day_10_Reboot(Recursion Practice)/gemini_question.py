#  Write a recursive function sum_natural(n) that calculates the sum of all numbers from n down to 1.


def sum_natural(n):
    if n == 0:
        return 0
    
    else:
        return n + sum_natural(n - 1)
    
print(sum_natural(5))