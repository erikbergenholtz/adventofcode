#!/usr/bin/env python3

import sys
import string

def findJunction(m, d, x, y):
    steps = 1
    x,y = x+d[0], y+d[1]
    ls = []
    while m[y][x] != "+" and m[y][x] != " ":
        steps += 1
        if m[y][x] in string.ascii_letters:
            ls.append(m[y][x])
        x,y = x+d[0], y+d[1]
    return (x,y), "".join(ls), steps

U,D,L,R = (0,-1),(0,1),(-1,0),(1,0)
def turn(m, d, x, y):
    global U,D,L,R
    dirs = [U, D, L, R]
    dirs.remove((-d[0], -d[1]))
    dirs.remove(d)
    for nd in dirs:
        ny, nx = y+nd[1], x+nd[0]
        if ny < 0 or nx < 0:
            continue
        if m[ny][nx] != " ":
            return nd
    return False

m = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        m.append(line)

pos = (m[0].index("|"), 0)
d = (0, 1)
ls = ""
ss = 0
while d != False:
    pos,tl,ts = findJunction(m, d, *pos)
    ls += tl
    ss += ts
    d = turn(m, d, *pos)

print(ls)
print(ss)
