#!/usr/bin/env python

print("Enter the first number:")
first = input()

try:
    first_val = int(first)
except ValueError:
    print("this input is not valid")
else: 
    print("Enter the second number:")
    second = input()
    try:
        sec_val = int(second)
    except ValueError:
        print("this input is not valid")
    else:
        result = first_val * sec_val
        print("%i * %i = %i" % (first_val, sec_val, result))
        if (result == 0):
            print("this number is both positive and negative")
        elif (result > 1):
            print("this number is positive")
        else:
            print("this number is negative")
