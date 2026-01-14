#!/usr/bin/env python

def greetings(str = "noble stranger"):
    if (isinstance(str, int) == False):
        print("Hello, " + str + ".")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
