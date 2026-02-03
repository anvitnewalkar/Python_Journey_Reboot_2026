def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z     # Please modify global z to 0.
    z = 0        # This will refer to global z and creates a local variable
    return c

z = 3
print(sum(10,20))
print(z)