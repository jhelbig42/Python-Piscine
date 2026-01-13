#!/usr/bin/env python

print("Enter a number")
usr_in = input()

try:
    val = int(usr_in)
except ValueError:
    print("Invalid input")
else:
    for index in range(10):
        print("%i * %i = %i" % (index, val, index*val))