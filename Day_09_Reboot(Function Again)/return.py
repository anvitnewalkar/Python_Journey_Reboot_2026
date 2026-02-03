"""def greet(name, ending):
    print('Good day '+ name)
    print(ending)
    return 'I love you saloni.'

greet('Anvit', 'Thankyou')

a = greet('Saloni', 'Thankyeeeewwwwww')

print(a)"""


def average():
    a = int(input("Enter your number:- "))
    b = int(input("Enter your number:- "))
    c = int(input("Enter your number:- "))

    average = (a + b + c) / 3
    # print(average)
    return f"The average of entered number is:- {average}"


a = average()
print(a)