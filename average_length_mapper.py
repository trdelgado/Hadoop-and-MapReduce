#!/usr/bin/python

import sys
import csv
from datetime import datetime
     
reader = csv.reader(sys.stdin, delimiter='\t',lineterminator='\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

for line in reader:
    node_id = line[0]
    node_type = line[5]
    body = line[4]
    if node_type == "question":
        print "{0}\t{1}\t{2}".format(node_id, node_type, len(body))
    elif node_type == "answer":
        abs_parent_id = line[7]
        print "{0}\t{1}\t{2}".format(abs_parent_id,node_type,len(body))
