"""def secret_agent():
    code_name = "007"
    print(f"Agent {code_name} is active.")

secret_agent()

# The Bug is here:
print(f"The agent's name is {code_name}")
"""

def secret_agent():
    code_name = "007"
    return code_name

print(f"The agent's name is {secret_agent()}")