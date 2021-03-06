#!/usr/bin/env python

import sys
import itertools

def extractData(fileName):
	data = []
	with open(fileName) as f:
		for line in f.readlines():
			data.append(map(int,line.strip().split()))
	return data

def isPossibleTriangle(p):
	if p[0] + p[1] > p[2]:
		return True
	return False

def nrPossibleTriangles(data):
	nrPossible = 0
	for item in data:
		permute = list(itertools.permutations(item))
		for p in permute:
			if not isPossibleTriangle(p):
				break
		else:
			nrPossible += 1
	return nrPossible

def main():
	if len(sys.argv) < 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	print nrPossibleTriangles(extractData(sys.argv[1]))
	return 0

if __name__ == '__main__':
	main()
