#!/usr/bin/env python

import sys
 
index = len(sys.argv)
if index == 1:
    print("none")
else:
    while index > 1:
        print(sys.argv[index - 1])
        index -= 1