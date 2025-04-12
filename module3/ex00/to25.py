#!/usr/bin/python3


num = input("Enter a number less than 25 \n")
num = int(num)
if num < 25:
    while num <= 25:
        print("Inside the loop, my variable is", num)
        num += 1
else:
    print("Error")
