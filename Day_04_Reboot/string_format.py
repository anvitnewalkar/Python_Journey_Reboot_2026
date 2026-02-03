# String Formating

template = "Dear {}, You are awesome. Take this {}$ bag"

a = "John"
a1 = 10000

b = "Jack"
b1 = 1000

c = "James"
c1 = 3000

s1 = template.format(a,a1)    # Return a formatted version of the string, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').
print(s1)

""" 

Note :- This method was used before python 3.6.

"""