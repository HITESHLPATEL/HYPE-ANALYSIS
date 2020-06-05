#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
	if(re.search(r'^\d{4}-\d{2}-\d{2}',line)):
		line = line.split(' ',2)
		line[2] = re.sub('http\S+\s*','',line[2])
		line[2] = re.sub(r'[^\w\s]', '',line[2])
		line[2] = re.sub('\s+', ' ', line[2])
		line[2] = line[2].strip()
		print ('%s,%s'%(line[0],line[2]))
		key=line[0]
	elif(re.search(r'^$',line)):
		continue
	else:
		line = re.sub('http\S+\s*','',line)
		line = re.sub(r'[^\w\s]', '',line)
		print('%s,%s'%(key,line))
		



		


	   
	