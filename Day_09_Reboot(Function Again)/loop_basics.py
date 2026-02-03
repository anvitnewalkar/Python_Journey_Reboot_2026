# Factorial suing while loop

"""n = int(input("Enter a number:-"))

result = 1

while(n > 0):
    result = result * n
    n -= 1  # n = n - 1

print(f"The factorial of entered number is:-{result}")
"""

# Factorial using for loop

n = int(input("Enter a number:-"))

result = 1

for i in range(1, n - 1):
    result = result * i