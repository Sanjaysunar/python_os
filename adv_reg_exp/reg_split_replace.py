import re

split_one = re.split(r"[.?!]","One sentence. Another one? And the last one!")
print(split_one)


split_two = re.split(r"([.?!])","One sentence. Another one? And the last one!")
print(split_two)

sub_one = re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]", "Received an email for go_nits95@my.example.com")
print(sub_one)

sub_two = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(sub_two)
