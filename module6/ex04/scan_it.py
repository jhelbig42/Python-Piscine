#!/usr/bin/env python

import sys

if (len(sys.argv) < 3):
    print("none")
else:
    nbr = (sys.argv[2]).count(sys.argv[1])
    if (nbr == 0):
        print("none")
    else:
        print(nbr)