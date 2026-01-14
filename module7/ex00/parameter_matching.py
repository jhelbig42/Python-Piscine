#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print("none")
else:
    if(input("what was the parameter? ") == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry ...")
