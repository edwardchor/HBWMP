#!/usr/bin/python
# -*- coding:utf-8 -*-
import pynlpir
import sys

pynlpir.open(encoding='utf-8')
nfile=open('negative.txt')
pfile=open('positive.txt')
nhash=[]
phash=[]

for eachline in nfile:
	temp=eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8')
	nhash.append(temp)
for eachline in pfile:
	temp=eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8')
	phash.append(temp)

#print phash[10]
#print nhash[10]

result={"positive":['pos'], "negative":['neg']}

test=open('./test.txt')

#input comes from STDIN (standard input)  
for line in sys.stdin:
# remove leading and trailing whitespace  
        #line = line.strip()
# split the line into words  
        words = pynlpir.segment(line,0)
#	for value in words:
#	print words
# increase counters  
        for word in words:
	#	word=word.replace('\n','').decode('utf-8')
	#	print word
        # write the results to STDOUT (standard output);  
        # what we output here will be the input for the  
        # Reduce step, i.e. the input for reducer.py  
        # tab-delimited; the trivial word count is 1  
		if word in nhash:
			result['negative'].append(word)
		elif word in phash:
			result['positive'].append(word)
print result			
