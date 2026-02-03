"""

1. Create a string variable name with your full name. Print:
The first character
The last character
The length of the string

"""

"""
name = "Anvit Newalkar"

print("first character:", name[0])
print("last character:", name[-1])
print("Length of the string:",len(name))
"""


"""

2. Concatenate two strings: "Hello" and "World" with a space in between.


"""

# str1 = "Hello"
# str2 = "World"

# print(str1 + " " + str2)
# print(str1,str2)
# print

"""
num = [1,2,3,4]
num.append([5,6])
print(len(num))

"""


"""

String Methods and Functions
 
1.Take the string  
" i love python programming " and:
Remove extra spaces from both ends
2. Convert it to title case
3. Count how many times "o" appears


2.Check if the string 

"123abc" is alphanumeric

"""

text = " i love python programming "
print(text.strip())
print(text.title())
print(text.count("o"))

text2 = "123abc"
print(text2.isalnum())