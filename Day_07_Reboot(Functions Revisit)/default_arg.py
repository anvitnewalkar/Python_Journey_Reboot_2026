def average (a = 9, b = 1):
    print("The average is:-", (a + b)/2)

# average()
average(4,5)

def name(fname, mname = "Vhatkar", lname = "Newalkar"):
    print('Hello', fname, mname, lname)

name('Saloni')

def sum (a, b, plus = 2):
    x = a + b + plus
    return x

c = sum(10, 5, 10)
print(c)