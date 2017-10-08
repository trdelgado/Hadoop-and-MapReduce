#!/usr/bin/python

import sys
import csv
from datetime import datetime
     
reader = csv.reader(sys.stdin, delimiter='\t',lineterminator='\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

for line in reader:
    node_id = line[0]
    abs_parent_id = line[7]
    author_id = line[3]
    question_type = line[5]
    if question_type == "question":
        writer.writerow([node_id, author_id])
    else:
        writer.writerow([abs_parent_id, author_id])
   
