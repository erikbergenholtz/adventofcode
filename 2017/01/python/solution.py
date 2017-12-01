#!/usr/bin/env python3

import sys
import os

if len(sys.argv) == 1:
    print("Too few arguments")
    sys.exit(2)
if not os.path.isfile(sys.argv[1]):
    print("File {} does not exist".format(sys.argv[1]))
    sys.exit(2)

with open(sys.argv[1]) as f:
    data = ''.join(f.read().splitlines())

s1,s2 = 0,0
for i,v in enumerate(data):
    if v == data[(i+1)%len(data)]:
        s1 += int(v)
    if v == data[(i+int(len(data)/2)) % len(data)]:
        s2 += int(v)
print("Task 1: {}".format(s1))
print("Task 2: {}".format(s2))
