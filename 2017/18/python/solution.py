#!/usr/bin/env python3

import sys


registers = {chr(x+ord('a')):0 for x in range(26)}
instrs = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        line = line.split()
        instrs.append((line[0], tuple(line[1:])))

def getValue(registers, x):
    if x in [chr(i+ord("a")) for i in range(26)]:
        return registers[x]
    else:
        return int(x)

last = 0
nxt = 0
while nxt in range(len(instrs)):
    (instr, args) = instrs[nxt]
    if   instr == "snd":
        last = int(registers[args[0]])
    elif instr == "set":
        registers[args[0]] = getValue(registers, args[1])
    elif instr == "add":
        registers[args[0]] += getValue(registers, args[1])
    elif instr == "mul":
        registers[args[0]] *= getValue(registers, args[1])
    elif instr == "mod":
        registers[args[0]] %= getValue(registers, args[1])
    elif instr == "rcv" and last != 0:
        registers[args[0]] = last
        break
    elif instr == "jgz" and registers[args[0]] > 0:
        nxt += getValue(registers, args[1])
        continue
    nxt += 1


print(last)

registers = ({chr(x+ord('a')):0 for x in range(26)},
             {chr(x+ord('a')):0 for x in range(26)})

registers[0]['p'] = 0
registers[1]['p'] = 1

nsnd1 = 0
snd = [[],[]]
nxt = [0,0]
waiting = [False, False]
terminated = [False, False]
deadlock = False
while not terminated[0] or not terminated[1]:
    for i in [0,1]:
        dn = 1
        if terminated[i] or nxt[i] not in range(len(instrs)):
            terminated[i] = True
            continue
        (instr, args) = instrs[nxt[i]]
        if instr == "snd":
            snd[i].append(getValue(registers[i], args[0]))
            if i == 1:
                nsnd1 += 1
        elif instr == "set":
            registers[i][args[0]] = getValue(registers[i], args[1])
        elif instr == "add":
            registers[i][args[0]] += getValue(registers[i], args[1])
        elif instr == "mul":
            registers[i][args[0]] *= getValue(registers[i], args[1])
        elif instr == "mod":
            registers[i][args[0]] %= getValue(registers[i], args[1])
        elif instr == "rcv":
            if len(snd[(i+1)%2]) > 0:
                waiting[i] = False
                registers[i][args[0]] = snd[(i+1)%2][0]
                del snd[(i+1)%2][0]
            else:
                waiting[i] = True
                if (waiting[(i+1)%2] or terminated[(i+1)%2]):
                    deadlock = True
                dn = 0
        elif instr == "jgz" and getValue(registers[i],args[0]) > 0:
            dn = getValue(registers[i], args[1])
        nxt[i] += dn
    if deadlock:
        break

print(nsnd1)
