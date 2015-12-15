# -*- coding:utf-8 -*-
#!/usr/bin/env python


import sys

#resfile = codecs.open('new_data.txt', 'w', 'utf-8')
resfile = open('new_data.txt', 'w')
cnt = 0
for line in sys.stdin:
    line = line.strip()
    print >> resfile, line
