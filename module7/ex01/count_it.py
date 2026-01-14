#!/usr/bin/env python

import sys

nbr = len(sys.argv)
if (nbr == 1):
    print("none")
else:
    print("parameters: ", nbr)
    for i in range(1, nbr):
        print(sys.argv[i], ":", len(sys.argv[i]))
