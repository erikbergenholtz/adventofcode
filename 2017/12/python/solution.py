#!/usr/bin/env python3

import sys

data = {}
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        line = line.replace(",","")
        line = line.replace("<->","")
        d = line.split()
        data[d[0]] = d[1:]

groups = set()
for k,v in data.items():
    progs = set()
    neighbours = [k]
    visited = []
    while len(neighbours) > 0:
        curr = min(neighbours)
        neighbours.remove(curr)
        visited.append(curr)
        for n in data[curr]:
            if n not in visited:
                neighbours.append(n)
            progs.add(n)
    if k == "0":
        print(len(progs))
    groups.add(frozenset(progs))
print(len(groups))
