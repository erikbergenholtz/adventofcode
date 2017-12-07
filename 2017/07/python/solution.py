#!/usr/bin/env python3

import sys

ps = {}

class Prog:
    def __init__(self, n, w, _hs):
        self.name    = n
        self.weight  = w
        self.holding = [h.replace(",","") for h in _hs[:]]

def gettowerweight(name):
    global ps
    ws = []
    ns = []
    if len(ps[name].holding) == 0:
        return ps[name].weight
    for h in ps[name].holding:
        ws.append(gettowerweight(h))
        ns.append(h)
    for i,v in enumerate(ws):
        if ws.count(v) == 1:
            x = ws[i + 1 if i==0 else -1]
            print(ps[ns[i]].weight + ((ws[i] - x)) * -1 if ws[i] > x else 1)
            sys.exit(0)
    ws.append(ps[name].weight)
    return sum(ws)

with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        d = line.split()
        n = d[0]
        w = int(d[1][1:-1])
        h = [] if len(d) == 2 else d[3:]
        ps[n] = (Prog(n,w,h[:]))

for k,p in ps.items():
    found = False
    for k,q in ps.items():
        if p.name in q.holding:
            found = True
    if not found:
        base = p.name
        break

print(base)
gettowerweight(base)
