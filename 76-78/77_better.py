'''
Solved using a better recurrence for the dynamic programming;
now we don't need to keep track of which sets we are actually
counting and so this will go literally exponentially faster

The core idea is to do a two-dimensional cache, where the variables
(n, k) are: n is the number, k is the largest prime used in the partition of n
'''
'''
Another argument in the forums notes that by just observing the numbers of partitions involving just 3, 5, and 7, 
the upper bound on the solution is 183, so only primes up to 177 are needed.
This makes loading the first million primes from disk a little overkill.
Anyway, I know from solving the problem in another way that really you only need 
primes up to 71.
'''
import sys
import pdb
import numpy as np

# I was not interested in writing a new sieve right now that would do generation up to n or anything
# Or even figuring out how to call my own sieve
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
          107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]

'''
There are several stylistic things here that come up when the recurrence is unintuitive.
It's cleanest to fill out the base cases first so that there are as few recurrence special cases as possible.
Since there are variable sized gaps between the primes, instead of just incrementing like with many partition problems,
there can be issues (e.g, subtract some stuff to find that your cache doesn't explicitly mention how many times you can use 3 in a partition of 2).
'''

'''
Example: I tried to factor out the access of the cache so that I could automatically get some bad values taken care of.
It turns out that 
a) Well, you'll need a few lines to handle special cases
b) How are you going to propagate return values, or if you don't use return values, will you call a function
to populate the cache and then afterwards access the cache? That's kind of stupid, right?
c) Taking this thing out into its own function means you have to replace breaks with returns, and maybe also you'll run into problems
because you don't have access to largest prime, or prime idx, or whatever. Perfectly ordinary problems to run into while refactoring,
but in the end it's not necessarily much cleaner.


def calculate_num_partitions(num, prime_idx, cache):
    largest_prime = primes[prime_idx]
    print(num, largest_prime)
    if (num, prime_idx) in cache:
        return cache[(num, prime_idx)]
    if largest_prime == num:
        cache[(num, prime_idx)] = 1
        return 1
    if largest_prime > num or largest_prime == num - 1:
        cache[(num, prime_idx)] = 0
        return 0
    if prime_idx == 0:
        num_partitions = cache[(num - largest_prime, prime_idx)]    
    else:
        next_largest_prime = primes[prime_idx - 1]
        num_partitions = calculate_num_partitions(num - largest_prime, prime_idx, cache) + \
                calculate_num_partitions(num - largest_prime + next_largest_prime, prime_idx - 1, cache)
    if num_partitions >= 5000:
        print(num)
        sys.exit()
    cache[(num, prime_idx)] = num_partitions
    return num_partitions


cache = {}
num = 2
while True:
    for prime_idx, largest_prime in enumerate(primes):
        res = calculate_num_partitions(num, prime_idx, cache)
        if res == 0:
            break
    num += 1
'''


'''
cache = {}
num = 4
cache[(2, 0)] = 1
cache[(3, 1)] = 1 # You have to do this or else the num - 1 condition above will trip early, skipping populating cache(3, 1) and giving it an implicit value of 0
while True:
    for prime_idx, largest_prime in enumerate(primes):
        if largest_prime == num:
            cache[(num, prime_idx)] = 1
            break
        if largest_prime > num or largest_prime == num - 1:
            cache[(num, prime_idx)] = 0
            break
        if prime_idx == 0:
            num_partitions = cache[(num - largest_prime, prime_idx)]    
        else:
            next_largest_prime = primes[prime_idx - 1]
            num_partitions = cache.get((num - largest_prime, prime_idx), 0) + cache.get((num - largest_prime + next_largest_prime, prime_idx - 1), 0)
        cache[(num, prime_idx)] = num_partitions
    if sum(y for x, y in cache.items() if x[0] == num) >= 5000: # this is massively ugly, just checking something rq
        pdb.set_trace()
        print(num, largest_prime)
        sys.exit()
    num += 1
'''

cache = np.zeros((1000, 100))
for idx, prime in enumerate(primes):
    cache[prime][idx] = 1 #It's better to populate all initial conditions explicitly when known. Otherwise we'd trip the same thing here as in the above solution.

num = 4
while True:
    last_prime = None
    for idx, prime in enumerate(primes):
        if prime >= num - 1:
            break
        num_partitions = cache[num - prime][idx]
        if last_prime is not None:
            num_partitions += cache[num - prime + last_prime][idx - 1]
        last_prime = prime
        cache[num][idx] = num_partitions
    if sum(cache[num]) >= 5000:
        print(num)
        sys.exit()
    num += 1
            
