#!/usr/bin/env python

count1 = 0

while count1 <= 10:
    print("table of %i: " % count1, end = "")
    count2 = 0
    while count2 <= 10:
        if count2 < 10:
            print("%i " % (count1 * count2), end = "")
        else:
            print("%i " % (count1 * count2))
        count2 += 1
    count1 +=1
    