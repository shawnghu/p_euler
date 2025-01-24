'''
I solved 77 before this one; it turns out they're basically the same idea when you get the DP phrased correctly
'''
import sys
import pdb
import numpy as np

cache = np.zeros((101, 101))
for x in range(101):
    cache[x][x] = 1

for num in range(101):
    for x in range(1, num):
        num_partitions = cache[num - x][x] + cache[num - 1][x - 1]
        cache[num][x] = num_partitions
print(sum(cache[5]) - 1)
