#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

for line in sys.stdin:
    line = unicode(line, 'utf-8')
    content = line.strip().split('\t')[5]
    print content.encode('utf-8')


