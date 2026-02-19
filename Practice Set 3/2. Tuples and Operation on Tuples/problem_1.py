"""
Create a tuple coordinates = (10, 20) and print both elements.

"""

coordinates = (10, 20)

print(coordinates[0])

print(coordinates[1])

"""
2. Try to modify the tuple by setting coordinates[0] = 50 — note what
happens.

"""

# coordinates[0] = 50

# print(coordinates)


""" 
Convert the tuple to a list, change its first element to 50 , and convert it back
to a tuple.

"""

corlist = list(coordinates)

corlist[0] = 50

coordinates = tuple(corlist)

print(coordinates)