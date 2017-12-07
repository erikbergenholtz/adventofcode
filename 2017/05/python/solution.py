#!/usr/bin/env python3

import sys

jumps  = []
jumps2 = []
n1     = 0
n2     = 0
index  = 0

with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        jumps.append(int(line))
        jumps2.append(int(line))

while index < len(jumps):
    jumps[index] += 1
    index += (jumps[index]-1)
    n1 += 1

index = 0
while 0 <= index and index < len(jumps2):
    tmp = jumps2[index]
    jumps2[index] += -1 if tmp >= 3 else 1
    index += tmp
    n2 += 1

print(n1)
print(n2)
