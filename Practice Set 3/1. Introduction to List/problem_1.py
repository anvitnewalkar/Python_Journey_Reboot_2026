"""1. Create a list fruits = ["apple", "banana", "cherry"] .

Print the first fruit.
Replace "banana" with "orange" .
Print the length of the list.

"""

fruits = ["apple", "banana", "cherry"]

print(fruits, "\n", type(fruits))

new_fruits = fruits.copy()

# print(new_fruits, "\n", type(new_fruits))

new_fruits[1] = "orange"

print(new_fruits)

print(len(new_fruits))