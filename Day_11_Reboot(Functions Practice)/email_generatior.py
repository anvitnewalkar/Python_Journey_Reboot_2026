# Write a function called make_email(first, last) that:

# Takes a first name and last name.

# Returns an email address in this format: first.last@company.com

# Bonus: Make sure the names are in lowercase (e.g., "Anvit" becomes "anvit").

# Example Input: make_email("Anvit", "Newalkar")

# Expected Output: anvit.newalkar@company.com



"""def make_email(first, last):
    temp_first = first.lower()
    temp_last = last.lower()
    email = f"{temp_first}.{temp_last}@gmail.com"

    return email

print(make_email("Anvit","Newalkar"))"""

# Another method

def make_email(first, last):
    return f"{first.lower()}.{last.lower()}@gmail.com"

print(make_email("Anvit","Newalkar"))