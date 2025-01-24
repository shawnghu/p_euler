'''
I solved 77 before this one; it turns out they're basically the same idea when you get the DP phrased correctly
This is also the same as 76 but with bigger numbers
'''
import sys
import pdb
import numpy as np
# import mpmath

#mpmath.mp.dps = 200

'''
I am bewildered to find that this solution actually still isn't good enough. The answer is at least 30000
so the size of the array required is at least 900 million, which even if you use uints isn't very good.
Also due to the non-locality of reference even the loop that I thought was pretty optimized isn't very good.
I think that I need an asymptotically superior solution; jkvz's solution appears to be O(n)ish instead of O(n^2)
somehow, but I can't use his code because it also relies somehow on some property of primes.

After the fact, I have learned that the answer was only 55374, so perhaps just optimizing this solution would have been sufficient.
'''
'''
def main():
    cache = np.zeros((30001, 30001), dtype=np.uint)
    for x in range(30001):
        cache[x][x] = 1

    for num in range(30001):
        total = 0
        if num % 200 == 0:
            print(num)
        for x in range(1, num):
            cache[num][x] = (cache[num - x][x] + cache[num - 1][x - 1]) % 1000000 # this is the core trick
            total += cache[num][x]
        if total % 1000000 == 0 and total != 0:
            print(num)
            sys.exit()
main()
'''

'''
O(n^(1.5) ish thing based on Euler's pentagonal number theorem.
I don't actually understand how this works, admittedly, and I'm not that tempted to
unless partitions become a lot more important in my life.
It is prompting me to look into generating functions, though.

Also, having looked at the forum after solving the problem, it seems that almost every single person
used Euler's pentagonal number theorem without understanding it, so it looks like I'm not alone here.
(A few just tried to optimize the standard DP solution)
'''

pentagonal_numbers = []
n = 1
while True:
    p = n * (3 * n - 1) / 2
    pentagonal_numbers.append(p)
    p = n * (3 * n + 1) / 2
    pentagonal_numbers.append(p)
    if p > 1000000:
        break
    n += 1

partitions_by_n = [1, 1]

idx = 2
while True:
    if idx % 5000 == 0:
        print(idx)
    partitions = 0
    x = 0
    for p in pentagonal_numbers:
        if p > idx:
            break
        partitions_p = partitions_by_n[int(idx - p)]
        if x % 4 == 2 or x % 4 == 3:
            partitions_p = - partitions_p
        partitions += partitions_p
        x += 1
    if partitions % 1000000 == 0:
        print(idx)
        sys.exit()
    partitions_by_n.append(partitions)
    idx += 1

