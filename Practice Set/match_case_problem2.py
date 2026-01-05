"""
WAP using match case that simulates a simple calculator

a) Ask the user for two numbers and an operation (+,-,*,/)

b) Perform the operation using match case

"""


num1 = int(input("Enter first number:- "))

num2 = int(input("Enter second number:- "))

operation = input("Choose opetration:- ")

match operation:
    case "+":
        print("Addition of two numbers is:- ",num1 + num2)
    
    case "-":
        print("Substraction of two numbers is:-",num1 - num2)

    case "*":
        print("Multiplication of two numbers is:- ",num1 * num2)

    case "/":
        print("Division of two numbers is:-",num1 / num2)

    