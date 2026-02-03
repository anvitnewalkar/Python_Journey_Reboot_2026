
# 1.Write a program that counts how many vowels are in a given string.



"""
name = "Anvit Newalkar"

count = 0

vowels = ['a','e','i','o','u','A','E','I','O','U']

for i in name:
    if i in vowels:
        count += 1

print(f"There are {count} vowels in this name")
"""



# 2.Take a user input string and check if it is a palindrome (same forwards and backwards).

character = input("Enter character:- ")

if character == character[::-1]:
    print("The string is Palindrome.")

else:
    print("The string is not a Palindrome.")