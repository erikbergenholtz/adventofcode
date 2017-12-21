#!/usr/bin/env python3

import sys
import re

def moveParticle(p, v, a):
    p = [p[i]+v[i] for i in range(len(p))]
    v = [v[i]+a[i] for i in range(len(p))]
    return [p,v,a]

ps = []

with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        res = re.findall(r'<([^>]*)>',line)
        vals = []
        for r in res:
            vals.append([int(x) for x in r.split(",")])
        ps.append(vals)

delta = []
for _ in range(1000):
    for i in range(len(ps)):
        ps[i] = moveParticle(ps[i][0], ps[i][1], ps[i][2])
        try:
            delta[i] = sum([abs(x) for x in ps[i][0]])
        except IndexError:
            delta.append(sum([abs(x) for x in ps[i][0]]))
print(delta.index(min(delta)))
