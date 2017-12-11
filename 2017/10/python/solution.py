#!/usr/bin/env python3

import sys
import operator
from functools import reduce

def twist(arr, l, h):
    a = [arr[i%len(arr)] for i in range(l,h)]
    for i in range(len(a)//2):
        a[i],a[len(a)-i-1] = a[len(a)-i-1],a[i]
    for i,j in enumerate(range(l,h)):
        arr[j%len(arr)] = a[i]
    return arr

def part1():
    twists = []
    arr = [i for i in range(256)]

    with open(sys.argv[1]) as f:
        twists = [int(x) for x in f.read().strip().split(",")]

    cur = 0
    step = 0
    for t in twists:
        arr = twist(arr, cur, (cur+t))
        cur += t + step
        step += 1

    print(arr[0] * arr[1])

def part2():
    twists = []
    arr = [i for i in range(256)]

    with open(sys.argv[1]) as f:
        twists = [ord(c) for c in f.read().strip()]
    twists += [17, 31, 73, 47, 23]
    cur = 0
    step = 0
    for i in range(64):
        for t in twists:
            arr = twist(arr, cur, (cur+t))
            cur += t + step
            step += 1
    hash = []
    for i in range(0,256,16):
        hash.append(reduce(operator.xor,arr[i:i+16]))
    for h in hash:
        sys.stdout.write("%.2X" % h)
    print()

part1()
part2()
