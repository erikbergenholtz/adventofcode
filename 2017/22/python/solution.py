#!/usr/bin/env python3

import sys

def expandMap(m, d, x, y):
    x += 1 if d == L else 0
    y += 1 if d == U else 0
    m.insert(0,list("."*len(m[0]))) if d == U else m.append(list("."*len(m[0])))
    for i in range(len(m)):
        m[i].insert(0,".") if d == L else m[i].append(".")
    return m, x, y

m = []
m2 = []

with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        m.append(list(line))
        m2.append(list(line))

U, D, L ,R = (0,-1), (0,1), (-1,0), (1,0)
lTurn = {U: L, L: D, D: R, R: U}
rTurn = {U: R, R: D, D: L, L: U}
C, I, W, F = '.', '#', 'W' ,'F'
change = {C: I, I: C}

virusPos = (len(m)//2,len(m[0])//2)
nInfected = 0
d = U

n = 10000
for _ in range(n):
    x, y = virusPos
    if not (y in range(len(m)) and x in range(len(m[0]))):
        m, x, y = expandMap(m, d, x, y)
    d = rTurn[d] if m[y][x] == I else lTurn[d]
    m[y][x] = change[m[y][x]]
    nInfected += 1 if m[y][x] == I else 0
    virusPos = (x+d[0], y+d[1])

print(nInfected)

change = {C: W, W: I, I: F, F:C}
virusPos = (len(m2)//2,len(m2[0])//2)
nInfected = 0
d = U

n = 10000000
for _ in range(n):
    x, y = virusPos
    if not (y in range(len(m2)) and x in range(len(m2[0]))):
        m2, x, y = expandMap(m2, d, x, y)
    s = m2[y][x]
    if s == C:
        d = lTurn[d]
    elif s == I:
        d = rTurn[d]
    elif s == F:
        d = rTurn[rTurn[d]]

    m2[y][x] = change[s]
    nInfected += 1 if m2[y][x] == I else 0
    virusPos = (x+d[0], y+d[1])

print(nInfected)
