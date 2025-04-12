#!/usr/bin/python3

n1 = input('Enter the first number:\n')
n2 = input('Enter the second number:\n')

n1 = int(n1)
n2 = int(n2)

result = n1 * n2

print(n1,'x',n2,'=',result)

if (result > 0):
    print("The result is positive.")
elif (result < 0):
    print("The result is negative.")
else:
    print("The result is both positive and negative.")
print()
