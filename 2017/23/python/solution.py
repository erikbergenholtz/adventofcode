#!/usr/bin/env python3

import sys

def getvalue(x):
    return regs[x] if x in regs.keys() else int(x)

regs = {x:0 for x in "abcdefgh"}
def set(x, y): regs[x]  = getvalue(y)
def sub(x, y): regs[x] -= getvalue(y)
def mul(x, y): regs[x] *= getvalue(y)
def jnz(x, y): return getvalue(y) if getvalue(x) else 1

instrs = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        line = line.split()
        instrs.append((locals()[line[0]], tuple(line[1:])))

nxt = 0
nmul = 0
while nxt in range(len(instrs)):
    (instr, (x,y)) = instrs[nxt]
    nd = instr(x, y)
    nxt += nd if instr.__name__ == "jnz" else 1
    nmul += 1 if instr.__name__ == "mul" else 0
print(nmul)

