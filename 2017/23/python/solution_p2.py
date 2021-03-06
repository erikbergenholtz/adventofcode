#!/usr/bin/env python3

# Found at https://stackoverflow.com/a/32882220
def isprime(number):
    return 2 in [number,2**number%number]

# Thanks to u/dario_p1 for posting their thought process on reddit!
# https://www.reddit.com/r/adventofcode/comments/7lo2ed/can_someone_exaplin_day_32_part_2/drnng2z/
h = 0
c = 126900
for b in range(109900, c+1, 17):
    if not isprime(b):
        h += 1
print(h)
