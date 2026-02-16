a = {3, 23, 1}

b = {23, 4, 2, 55, 1}

c = a.union(b)    # Return a new set with elements from the set and all others.

print(c)

d = a.intersection(b)  # Return a new set with elements common to the set and all others.

print(d)

print(a.pop())

print(a.discard(23))