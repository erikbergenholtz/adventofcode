#!/usr/bin/env python3

import sys

mem = []
theState = []
states = []
n = 0
found = 0

with open(sys.argv[1]) as f:
    line = f.read().split()
    mem = [int(l) for l in line]

while True:
    val = max(mem)
    bank = mem.index(val)
    mem[bank] = 0
    while val > 0:
        bank = (bank + 1)%len(mem)
        mem[bank] += 1
        val -= 1
    n += 1
    if found == 0 and mem in states:
        print(n)
        found = 1
        n = 0
        theState = mem[:]
    elif found == 1 and theState == mem:
        print(n)
        break
    else:
        states.append(mem[:])
