#!/usr/bin/env python

import sys

def upcase_it(str):
    return (str.lower())

#####

nbr = len(sys.argv)
if (nbr == 1):
    print("none")
else:
    for i in range(1, nbr):
        print(upcase_it(sys.argv[i]))
