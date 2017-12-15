#!/usr/bin/env python3

import sys

layers = {}
depth = 0
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        data = [int(x) for x in line.replace(":","").split()]
        layers[data[0]] = data[1]
    depth = data[0]+1

severity = 0
for i in range(depth):
    if i in layers:
        if i%((layers[i]-1)*2) == 0:
            severity += (i*layers[i])
print(severity)


delay = 0
while(True):
    found = False
    for i in range(depth):
        if i in layers:
            if (i+delay)%((layers[i]-1)*2) == 0:
                found = True
                break
    if not found:
        break
    delay += 1

print(delay)
