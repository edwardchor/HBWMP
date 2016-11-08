# -*- coding:utf-8 -*-
#!/usr/bin/env python

import sys

nfile=open('negative.txt')
pfile=open('positive.txt')
nhash=[]
phash=[]

resfile=open('split_result.txt','w')
for eachline in nfile:
        nhash.append(eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8'))
for eachline in pfile:
        phash.append(eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8'))

#print phash[10]
#print nhash[10]

result={'positive':['pos'],'negative':['neg']}
#print sys.stdin
#print type(line)
for line in sys.stdin:
	print line
	resfile.write(line)
#	line=line.strip()
#	for value in line:		
#		if value in phash:
    		#print '%s\t%s' % ('positive',value)
#			print value
#			print 'posiitve'
#			result['positive'].append(value)
#		elif value in nhash:
#			print value
			#print '%s\t%s' % ('negative',value)
#			print 'negative'
#			result['negative'].append(value)

#print result['positive']
#print result['negative']
