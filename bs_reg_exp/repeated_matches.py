import re

print(re.search(r"Py.n" , "Pygmalion"))

print(re.search(r"Py.*n" , "Pygmalion"))
 
print(re.search(r"Py.*n" , "Python Programming"))
 
print(re.search(r"Py[a-z]*n" , "Python Programming"))
 
print(re.search(r"Py[a-z]*n" , "Pyn"))
 
print(re.search(r"o+l+" , "goldfish"))

print(re.search(r"o+l+" , "wolly"))

print(re.search(r"o+l+" , "boil"))
 
print(re.search(r"o+l+" , "To each"))

print(re.search(r"p?each" , "To each"))

print(re.search(r"p?each" , "peaches"))


