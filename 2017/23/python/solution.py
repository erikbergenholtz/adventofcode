#!/usr/bin/env python3

import sys

# Found at https://stackoverflow.com/a/32882220
def isprime(number):
    return 2 in [number,2**number%number]

def getValue(registers, x):
    if x in [chr(i+ord("a")) for i in range(26)]:
        return registers[x]
    else:
        return int(x)

instrs = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        line = line.split()
        instrs.append((line[0], tuple(line[1:])))

registers = {chr(x+ord('a')):0 for x in range(8)}
nxt = 0
nmul = 0
while nxt in range(len(instrs)):
    (instr, args) = instrs[nxt]
    if instr == "set":
        registers[args[0]] = getValue(registers, args[1])
    elif instr == "sub":
        registers[args[0]] -= getValue(registers, args[1])
    elif instr == "mul":
        nmul += 1
        registers[args[0]] *= getValue(registers, args[1])
    elif instr == "jnz" and getValue(registers,args[0]) != 0:
        nxt += getValue(registers, args[1])
        continue
    nxt += 1
print(nmul)

# Thanks to u/dario_p1 for posting their thought process on reddit!
# https://www.reddit.com/r/adventofcode/comments/7lo2ed/can_someone_exaplin_day_32_part_2/drnng2z/
h = 0
c = 126900
for b in range(109900, c+1, 17):
    if not isprime(b):
        h += 1
print(h)
