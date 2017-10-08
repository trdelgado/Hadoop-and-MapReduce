import csv
 
def get_tags_dict(f):
    d = {}
    reader = csv.reader(f, delimiter='\t')
    reader.next() # skip header line
    for line in reader:
        tags_data = line[2]
        if line[5] != 'question': continue
        tags = tags_data.split()
        for tag in tags:        
            if tag in d:
              d[tag] += 1
            else:
              d[tag] = 1    
    return d


f = open("../../forum_node.tsv")
data = get_tags_dict(f)
f.close()
data = sorted(data.items(), key=lambda x: x[1], reverse=True)
for item in data[:10]:
  print item[0], "\t", item[1]
  

