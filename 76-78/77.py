import numpy as np
import pdb
from sortedcontainers import SortedList

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}

ways = {}
num = 2
'''
this feels kind of gross because i feel that i'm adding an entire O(n) or something by missing a trick,
but i'm pretty sure this will be sufficient for a problem this small.
'''
while True:
    total = 0
    waysfornum = []
    wayscheck = {}
    for prime in firstprimes:
        if prime == num:
            waysfornum.append(SortedList([prime]))
            break
        if prime > num or prime == num - 1:
            break
        for way in ways[num - prime]:
            new_way = way.copy()
            new_way.add(prime)
            t = tuple(new_way)
            if t in wayscheck:
                continue
            waysfornum.append(new_way)
            wayscheck[t] = True
    if len(waysfornum) > 5000:
        print(num)
        break
    ways[num] = waysfornum
    num += 1

