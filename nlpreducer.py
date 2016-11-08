# -*- coding:utf-8 -*-
#!/usr/bin/env python

import sys

resfile = open('result.txt', 'w')

for line in sys.stdin:
    line = line.strip()
    print >> resfile, line
