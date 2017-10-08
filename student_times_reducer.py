#!/usr/bin/python

import sys


import sys

hour_count = [0]*24
oldAuthor = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisAuthor, thisHour = data_mapped

    if oldAuthor and oldAuthor != thisAuthor:
        max_hour = max(hour_count)
        for i in range(0, len(hour_count)):
            if hour_count[i] == max_hour:
                print oldAuthor, "\t", i, "\t",max_hour 
        oldAuthor = thisAuthor
        hour_count = [0]*24

    oldAuthor = thisAuthor
    hour_count[int(thisHour)] += 1

if oldAuthor != None:
    max_hour = max(hour_count)
    for i in range(0, len(hour_count)):
        if hour_count[i] == max_hour:
            print oldAuthor, "\t", i, "\t",max_hour 
    
