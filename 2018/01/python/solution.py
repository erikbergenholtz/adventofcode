#!/usr/bin/env python3

import sys
from itertools import cycle

frequency = 0
freq_list = []
task_1 = None
task_2 = None
i = 0
with open(sys.argv[1]) as f:
    nlines = len(f.readlines())
    while not task_2:
        for line in f.readlines():
            if not task_2 and frequency in freq_list:
                task_2 = frequency
                break;
            freq_list.append(frequency)
            frequency += int(line)
            if i == nlines:
                task_1 = frequency
            i += 1

print("Task 1: {}".format(task_1))
print("Task 2: {}".format(task_2))
