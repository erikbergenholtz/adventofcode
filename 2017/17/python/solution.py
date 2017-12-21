#!/usr/bin/env python3

import sys
import blist

buf = blist.blist([0])
cur = 0

step = int(sys.argv[1])

for i in range(1,2018):
    cur = (cur+step)%len(buf)
    buf.insert(cur+1,i)
    cur = (cur+1)%len(buf)

print(buf[buf.index(2017)+1])

for i in range(2018,50000000):
    cur = (cur+step)%len(buf)
    buf.insert(cur+1,i)
    cur = (cur+1)%len(buf)
print(buf[buf.index(0)+1])
