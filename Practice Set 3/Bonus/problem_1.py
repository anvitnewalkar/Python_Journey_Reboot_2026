""" 
Write a program that takes a list of numbers and removes all duplicates using
a set.

"""

numbers = [15, 20, 15, 30, 45, 20, 50, 15]

print(f"Orginal numbers:- {numbers}")

new_numbers = set(numbers)

clean_set = list(new_numbers)

print(clean_set)


