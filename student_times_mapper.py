#!/usr/bin/python
import sys
import csv
from datetime import datetime
     
reader = csv.reader(sys.stdin, delimiter='\t',lineterminator='\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
     
reader.next()
    
for line in reader:
    if len(line) == 19:
        author_id = line[3]
        added_at = line[8]
        #added_at format is: 2012-02-23 09:15:02.270861+00
        hour = datetime.strptime(added_at.split("+")[0], '%Y-%m-%d %H:%M:%S.%f').hour
        print "{0}\t{1}".format(author_id, hour)
