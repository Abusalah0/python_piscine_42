#!/usr/bin/python3

num = input("Give me a number: ")

if num.isdigit():
    if num.find(".") != -1:
        print("This number is a decimal.")
    else:
        print("This number is an integer.")