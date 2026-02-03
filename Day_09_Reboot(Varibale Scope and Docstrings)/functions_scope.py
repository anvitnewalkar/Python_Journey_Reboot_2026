def sum(a, b):
    # a and b are local variables. It means you can access them inside a function.
    c = a + b
    print(z)
    return c

# global variable. It means you can access these variable outside a function or inside which is globally.
z = 8  
print(sum(4, 6))
# print(z)



def add(c, d):
    e = c + d
    z = 8   # It creates a local variable called z which is destroyed after this functions returns 
    return e

z = 69
print(add(24, 28))
print(z)
