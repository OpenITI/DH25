"""
This script showcases some string methods.

Run the script, and compare the output with the code.

For each string method, describe what it does
in a comment on the line above the code.

Remember: comments start with a hash (#) and are ignored by Python
"""

example = """You will rejoice to hear that no disaster has accompanied the
commencement of an enterprise which you have regarded with such evil
forebodings. I arrived here yesterday, and my first task is to assure
my dear sister of my welfare and increasing confidence in the success
of my undertaking."""

print("1. str.lower()")

# (write your comment here)
output = example.lower()
print(output)

print("-" * 10)
print("2. str.upper()")

# 
output = example.upper()
print(output)

print("-" * 10)
print("3. str.count()")

# 
output = example.count("my")
print(output)

print("-" * 10)
print("4. str.find()")

#
output = example.find("You")
print(output)
output = example.find("you")
print(output)
output = example.find("undertaking")
print(output)
output = example.find("Lollapolooza")
print(output)

print("-" * 10)
print("5. str.replace()")

# 
output = example.replace(". ", ".\n")
print(output)

print("-" * 10)
print("6. str.split()")

# 
output = example.split(". ")
print(output)

