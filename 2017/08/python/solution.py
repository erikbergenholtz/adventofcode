#!/usr/bin/env python

import sys
import operator
class Cond:
    def __init__(self,a,b,op):
        self.a = a
        self.b = int(b)
        self.op = op

class Instr:
    def __init__(self,r, v, c):
        self.reg = r
        self.val = v
        self.cond = Cond(c[0],c[2],c[1])

ops = {
        "==" : operator.eq,
        "!=" : operator.ne,
        ">=" : operator.ge,
        "<=" : operator.le,
        ">"  : operator.gt,
        "<"  : operator.lt,}
regs = {}
instrs = []

with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        d = line.split()
        n = d[0]
        v = int(d[2]) * (1 if d[1] == "inc" else -1)
        c = d[4:]
        regs[n] = 0
        instrs.append(Instr(n,v,c))

highest = 0
for i in instrs:
    if(ops[i.cond.op](regs[i.cond.a],i.cond.b)):
        regs[i.reg] += i.val
        if regs[i.reg] > highest:
            highest = regs[i.reg]

print(regs[max(regs, key=regs.get)])
print(highest)
