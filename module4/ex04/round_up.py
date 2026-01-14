#!/usr/bin/env python

try:
    inp = float(input("Give me a number: "))
except ValueError:
    print("input invalid")
else:
    if (inp == int(inp)):
        print(int(inp))
    else:
        print(int(inp + 1))