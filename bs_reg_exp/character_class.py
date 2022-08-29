import re

print(re.search(r"[Pp]ython","Python"))


print(re.search(r"[a-z]way","highway"))

print(re.search(r"[a-z]way","way"))

print(re.search("cloud[a-zA-Z0-9]","cloudy"))

print(re.search("cloud[a-zA-Z0-9]","cloud9"))

print(re.search("cat|dog","I like cats."))

print(re.search("cat|dog","I like dogs."))

print(re.search("cat|dog","I like both dogs and cats."))

print(re.findall("cat|dog","I like both dogs and cats.",))

