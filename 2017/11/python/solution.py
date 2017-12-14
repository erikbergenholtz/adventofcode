#!/usr/bin/env python3

import sys

dirs = {'n' : ( 0,  1, -1),
        'ne': ( 1,  0, -1),
        'se': ( 1, -1,  0),
        's' : ( 0, -1,  1),
        'sw': (-1,  0,  1),
        'nw': (-1,  1,  0),}
instrs = []

def addHex(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def hexDist(a,b):
    return sum([abs(a[i]-b[i]) for i in [0,1,2]])//2

with open(sys.argv[1]) as f:
    instrs = f.read().strip().split(",")

curr = (0,0,0)
dist = []
for instr in instrs:
    curr = addHex(curr, dirs[instr])
    dist.append(hexDist((0,0,0), curr))
print(hexDist((0,0,0), curr))
print(max(dist))
