#!/usr/bin/python3

print("Enter a number")
num = input()

num = float(num)

for i in range(0, 10):
    print(f'{i} x {num} = {i * num}')
