#!/usr/bin/env python

try:
    inp = float(input("Give me a number: "))
except ValueError:
    print("input invalid")
else:
    if (inp == int(inp)):
        print("this is an integer")
    else:
        print("this number is a decimal")
