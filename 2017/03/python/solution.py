#!/usr/bin/env python3

import sys
import math

N, E, S, W = (-1,0), (0,-1), (1,0), (0,1)
turn = {N:E, E:S, S:W, W:N}
d = S

n = int(sys.argv[1])
w = h = math.ceil(math.sqrt(n))

mem = [ [ 0 for i in range(w) ] for i in range(h) ]

def populate(n):
    global d
    x = w//2
    y = h//2
    for i in range(1,n+1):
        mem[x][y] = i
        dx,dy = turn[d]
        if (x+dx)<len(mem) and (y+dy)<len(mem[x]) and mem[x+dx][y+dy] == 0:
            d = turn[d]
        dx,dy = d
        x += dx
        y += dy
    return

def printmem():
    for m in mem:
        print(m)
    print()
printmem()
populate(n)
printmem()
