#!/usr/bin/python

import sys
import csv

oldKey = None
studentList = []


# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

reader = csv.reader(sys.stdin, delimiter='\t',lineterminator='\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 2:
        continue

    node_id = line[0]
    author_id = line[1]

    if oldKey and oldKey != node_id:
        writer.writerow([oldKey, studentList])
        studentList = []
        
    oldKey = node_id
    studentList.append(author_id)
 
if oldKey != None:
    writer.writerow([oldKey, studentList])
