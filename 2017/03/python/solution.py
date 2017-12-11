#!/usr/bin/env python3

import sys
import math

N, E, S, W = (0,1), (-1,0), (0, -1), (1, 0)
turn = {N:E, E:S, S:W, W:N}

def getSquareSum(mem, x, y):
    xs = [i for i in range(x-1,x+2) if i >=0 and i<len(mem)]
    ys = [i for i in range(y-1,y+2) if i >=0 and i<len(mem)]
    s = 0
    for x2 in xs:
        for y2 in ys:
            s += mem[x2][y2]
    return s

def getNextStep(mem,x,y,d,side):
    nX = x+turn[d][0]
    nY = y+turn[d][1]
    if nX in range(side) and nY in range(side) and mem[nX][nY] == 0:
        d = turn[d]
        x,y = nX,nY
    else:
        x += d[0]
        y += d[1]
    return x,y,d

def populateMemory(mem, num, side):
    x = y = side//2
    d = W
    for i in range(1,num+1):
        mem[x][y] = i
        x,y,d = getNextStep(mem, x, y, d,side)
    return mem

def populateMemory2(mem, num, side):
    x = y = side//2
    d = W
    mem[x][y] = 1
    for i in range(1,num+1):
        sqr = getSquareSum(mem, x, y)
        if sqr > num:
            return sqr
        mem[x][y] = sqr
        x,y,d = getNextStep(mem,x,y,d,side)

def getPosition(mem, num):
    x = [x for x in mem if num in x][0]
    return mem.index(x), x.index(num)

num = int(sys.argv[1])
h = math.ceil(math.sqrt(num))
if h%2 == 0:
    h += 1
half = h//2

mem = [[0 for i in range(h)] for i in range(h)]
mem = populateMemory(mem, num, h)
x,y = getPosition(mem, num)
steps = (abs(half-x)+abs(half-y))
print(steps)

mem = [[0 for i in range(h)] for i in range(h)]
print(populateMemory2(mem, num, h))
