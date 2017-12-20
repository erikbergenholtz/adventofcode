#!/usr/bin/env python3

import sys

buf = [0]
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
    if i%1000000 == 0:
        sys.stdout.write("\r%.2f%%" % ((i/50000000)*100))
print(buf[buf.index(0)+1])
