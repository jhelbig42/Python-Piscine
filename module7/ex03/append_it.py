#!/usr/bin/env python

import sys 

nbr = len(sys.argv)
if (nbr == 1):
    print("none")
else:
    for i in range(1, nbr):
        if (not sys.argv[i].endswith("ism")):
            print(sys.argv[i] + "ism")
        else:
            continue

