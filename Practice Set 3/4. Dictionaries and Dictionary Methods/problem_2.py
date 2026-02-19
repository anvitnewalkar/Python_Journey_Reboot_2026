"""
Create a dictionary of three friends and their phone numbers. Use:
keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them

"""

my_dict = {
    "Andy": 9090909090,
    "Shanks": 989379239,
    "Luffy": 7340897421
}

print(my_dict.keys())

print(my_dict.values())

for key, value in my_dict.items():
    print(key, value)