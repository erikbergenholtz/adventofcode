#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1]) as f:
    line = f.read().strip()

line = re.sub(r'!.',"",line)
garbage = re.findall(r'<[^>]*>',line)
nGarbage = 0
for g in garbage:
    nGarbage += len(g)-2
line = re.sub(r'<[^>]*>',"",line)
line = re.sub(r',',"",line)

score = 0
depth = 0
for c in line:
    if c == "}":
        depth -= 1
    else:
        depth += 1
        score += depth
print(score)
print(nGarbage)
