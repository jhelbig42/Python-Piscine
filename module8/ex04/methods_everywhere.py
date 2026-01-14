#!//usr/bin/env python

import sys

def shrink(str):
    return(str[0:8])

def enlarge(str, l):
    return(str + ((8 - l) * "Z"))

param = len(sys.argv)
if (param == 1):
    print("none")
else:
    for i in range(1, param):
        l = len(sys.argv[i])
        if (l == 8):
            print(sys.argv[i])
        elif (l < 8):
            print(enlarge(sys.argv[i], l))
        else:
            print(shrink(sys.argv[i]))