#!/usr/bin/env python3

file = open("spider.txt")
print(file.readline())

print(file.read())

file.close()

with open("spider.txt") as file:
    print(file.readline())

