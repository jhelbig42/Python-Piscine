#!/usr/bin/env python

number = input()

try:
    value = int(number)
except ValueError:
    print("this is not valid input")
    
else:
    if (value == 0):
        print("this number is both positive and negative")
    elif (value > 0):
        print("this number is positive")
    else:
        print("this number is negative")
