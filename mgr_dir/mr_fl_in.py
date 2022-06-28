import os

print(os.path.getsize("spider.txt"))

print(os.path.getmtime("spider.txt"))


import datetime

timestamp = os.path.getmtime("spider.txt")

print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("spider.txt"))
