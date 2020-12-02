#!/usr/bin/env python3

import sys

def solve1(fname):
    num = 0
    with open(fname, "r") as f:
        for line in f.readlines():
            l = line.strip().split(' ')
            r = [int(x) for x in l[0].split('-')]
            n = range(r[0],r[1]+1)
            c = l[1][0]
            if l[2].count(c) in n:
                num+=1
    return num

def solve2(fname):
    num = 0
    with open(fname, "r") as f:
        for line in f.readlines():
            l = line.strip().split(' ')
            n = [int(x)-1 for x in l[0].split('-')]
            c = l[1][0]
            p = l[2]
            if p[n[0]] != p[n[1]] and (p[n[0]] == c or p[n[1]] == c):
                num+=1
    return num

def main():
    fname = sys.argv[1]
    print(solve1(fname))
    print(solve2(fname))
    return 0

if __name__ == '__main__':
    sys.exit(main())
