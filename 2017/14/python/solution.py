#!/usr/bin/env python3

import knothash
import sys

visited = []
nGroups = 0

def findGroups(grid, x, y, inGroup=True):
    global visited
    global nGroups
    if x not in range(128) or y not in range(128):
        return
    if grid[x][y] == 0:
        return
    if (x,y) in visited:
        return
    visited.append((x,y))
    if not inGroup:
        nGroups += 1
    findGroups(grid, x+1, y)
    findGroups(grid, x-1, y)
    findGroups(grid, x, y+1)
    findGroups(grid, x, y-1)

data = sys.argv[1]

n = 0
grid = [ [ 0 for i in range(128)] for i in range(128)]
for i in range(128):
    checksum = knothash.knothash(data+"-{}".format(i))
    value = int(checksum, 16)
    j = 0
    while value > 0:
        n += 1 if value%2==1 else 0
        grid[i][j] = 1 if value%2 == 1 else 0
        j += 1
        value >>= 1

for i, cols in enumerate(grid):
    for j, val in enumerate(cols):
        if val == 1 and (i,j) not in visited:
            findGroups(grid,i,j,False)
print(n)
print(nGroups)
