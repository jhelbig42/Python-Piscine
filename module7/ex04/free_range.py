#!/usr/bin/env python

import sys

if (len(sys.argv) != 3):
    print("none")
else:
    try:
        first = int(sys.argv[1])
        second = int(sys.argv[2])
    except ValueError:
        print("non numerical values")
    else:
        if (second < first):
            print("second number is smaller than first")
        else:
            arr = []
            for i in range(first, (second + 1)):
                arr.append(i)
            print(arr)