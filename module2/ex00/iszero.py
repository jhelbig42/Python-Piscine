#!/usr/bin/env python

number = input()

try:
    value = int(number)
except ValueError:
    print("this is not valid input")
    
else:
    if (value == 0):
        print("this number is equal to zero")
    else:
        print("this number is different from zero")