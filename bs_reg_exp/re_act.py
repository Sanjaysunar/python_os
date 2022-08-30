import re

print(re.search(r"A.*a","Argentina"))

print(re.search(r"A.*a","Azerbaijan"))

print(re.search(r"^A.*a$","Azerbaijan"))

print(re.search(r"^A.*a$","Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern,"_this_is_valid"))

print(re.search(pattern,"this isn't valid"))

print(re.search(pattern,"valid1"))

print(re.search(pattern,"2valid1"))
