# There are two types of modules:-

# 1. Built in Modules

# 2. External modules

# List of all built in modules  https://docs.python.org/3/py-modindex.html

# Request Module link https://pypi.org/project/requests/

import math

print(f"The squareroot of a given number is {math.sqrt(16)}")

import my_module

my_module.greet()

import requests
r = requests.get("https://www.google.com")
print(r.text) 