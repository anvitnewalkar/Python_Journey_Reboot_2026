# 3. Lambda Functions

# 1. Write a lambda function that adds two numbers and test it.

"""add = lambda x, y: x + y

print(f"addition of numbers x and y is:{add(10,20)}")"""


#######################################################################################



# 2. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares

x = [1, 2, 3, 4, 5]

square = lambda x: x * x
print(map(square,x))