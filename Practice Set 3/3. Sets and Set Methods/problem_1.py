""" 
Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to
duplicate 3 ?)

"""

my_set ={1, 2, 3, 3, 4}

print(my_set)

# Set is unordered and has unique elements. The reason behind 3 is not printed again because set doesn't allow duplicate elements.

"""
Add 5 to the set, remove 2 , and check if 4 is in the set.

"""

my_set.add(5)

my_set.remove(2)

print(my_set)