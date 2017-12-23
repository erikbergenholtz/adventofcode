#!/usr/bin/env python3

import sys

def spin(ps, a):
    return ps[-a:] + ps[:-a]

def exchange(ps, a, b):
    ps[a], ps[b] = ps[b], ps[a]
    return ps

def partner(ps, a, b):
    ia, ib = ps.index(a), ps.index(b)
    ps[ia], ps[ib] = ps[ib], ps[ia]
    return ps

moves = {'s': spin,
         'x': exchange,
         'p': partner,}

instrs = []
with open(sys.argv[1]) as f:
    for instr in f.read().strip().split(","):
        try:
            instrs.append((instr[0],tuple([int(i) for i in instr[1:].split("/")])))
        except:
            instrs.append((instr[0],tuple(tuple(instr[1:].split("/")))))

progs = [chr(i+ord("a")) for i in range(16)]
for m,a in instrs:
    progs = moves[m](progs, *a)
print("".join(progs))

n = 1000000000
seen = []
noNew = 0
progs = [chr(i+ord("a")) for i in range(16)]
for i in range(n):
    seen.append("".join(progs))
    for m,a in instrs:
        progs = moves[m](progs, *a)
    if "".join(progs) in seen:
        print(seen[n%len(seen)])
        break
