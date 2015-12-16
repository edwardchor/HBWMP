#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import pdb

nfile=open('negative.txt')
pfile=open('positive.txt')
nhash=[]
phash=[]

def GetWords(sent):
    ret = []
    l = len(sent)
    for p in range(0, 7):
        for i in range(0, l-p):
            ret.append(sent[i:i+p+1])
    return ret

for eachline in nfile:
	temp=eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8')
	nhash.append(temp)
for eachline in pfile:
	temp=eachline.replace('\xef\xbb\xbf','').replace('\n','').decode('utf-8')
	phash.append(temp)

for line in sys.stdin:
    line = line.strip()
    line = unicode(line, 'utf-8')
    words = GetWords(line)
    score = 0
    for word in words:
        score += 1 if word in phash else 0
    print line.encode('utf-8'), '\t', 'pos' if score > 0 else 'neg'
