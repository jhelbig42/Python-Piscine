#!/usr/bin/env python

print("Enter a number less than 25")
usr_in = input()

try:
    val = int(usr_in)
except ValueError:
    print("Invalid input")
else:
    if( val > 24):
        print("not  a number below 25")
    else:
        while (val <= 25):
            print("inside the loop, my variable is %i" % val)
            val = val + 1