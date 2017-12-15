#!/usr/bin/env python3

import sys

def samelower16(a,b):
    return a&0xffff == b&0xffff

def printprogress(i,n):
    if i%100000 == 0:
        sys.stdout.write("\r%.2f%%"%((i/n)*100))

def generate(p, f):
    return ((p[0]*f[0])%2147483647, (p[1]*f[1])%2147483647)

def duel(n,factors, seeds):
    nPairs = 0
    previous = seeds
    for i in range(n):
        previous = (a,b) = generate(previous,factors)
        nPairs += 1 if samelower16(a,b) else 0
        printprogress(i,n)
    return nPairs

def duel2(n, factors, seeds):
    nPairs = 0
    previous = seeds
    i = 0
    keepA = keepB = -1
    while(i < n):
        a,b = generate(previous, factors)
        keepA = a if a%4==0 and keepA == -1 else keepA
        keepB = b if b%8==0 and keepB == -1 else keepB
        if -1 not in (keepA, keepB):
            nPairs += 1 if samelower16(keepA, keepB) else 0
            previous = (keepA, keepB)
            keepA = keepB = -1
            i += 1
            printprogress(i,n)
            continue
        previous = (a,b)
    return nPairs

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    seeds = (int(lines[0].split()[-1]), int(lines[1].split()[-1]))
factors = (16807, 48271)

print("\n{}".format(duel(40000000, factors, seeds)))
print("\n{}".format(duel2(5000000, factors, seeds)))
