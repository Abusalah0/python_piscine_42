#!/usr/bin/python3

words = input()

for i in words:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
print()
