import re

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng","clapping"))

print(re.search(r"p.ng","Pangaea", re.IGNORECASE))

