'''
This one doesn't actually work within the allotted one minute.
I accidentally left it running overnight, and found the answer, and didn't want to come back to it.
There are several obvious optimizations to make so that it will run in time, e.g, the loops for finding the higher order tuples don't need to go over all primes,
but just all existing pairs.
Also, the later loops take suspiciously long per iteration.
This marks the first PE problem I had to actively profile.
'''
from utils.prime_utils import isprime
import numpy as np
import pdb
import sys
import math
import line_profiler
profile = line_profiler.LineProfiler()


def index_generator():
    for a in range(1, 1000):
        for b in range(1, a):
            for c in range(1, b):
                for d in range(1, c):
                    for e in range(1, d):
                        yield [a, b, c, d, e]

# index_gen = index_generator()

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_10million_primes.npy')
diprimes = {x: True for x in firstprimes}
# pdb.set_trace()

#@profile
def test_concatenation_property_pair(prime_a, prime_b):
    # if not isprime(int(str(prime_a) + str(prime_b)), diprimes, 15485863):
    candidate = int(str(prime_a) + str(prime_b))
    # candidate = prime_a * (10 ** (math.floor(math.log(prime_b, 10)) + 1)) + prime_b # not faster
    if candidate not in diprimes:
        return False
    candidate = int(str(prime_b) + str(prime_a))
    if candidate not in diprimes:
    # if not isprime(int(str(prime_b) + str(prime_a)), diprimes, 15485863):
        return False
    return True

# print(test_concatenation_property((3, 7, 109, 673)))

# @profile
def generate_prime_pairs():
    prime_pairs = {}
    for a in range(1, 10000):
        prime_a = firstprimes[a]
        if a % 100 == 0:
            print('a = %d' % a)
        for b in range(1, a):
            prime_b = firstprimes[b]
            if test_concatenation_property_pair(prime_a, prime_b):
                prime_pairs[(firstprimes[a], firstprimes[b])] = True
    print('created %d prime 2-tuples' % len(prime_pairs))
    return prime_pairs

prime_pairs = generate_prime_pairs()
# pdb.set_trace()

prime_3tuples = {}
for c in range(1, 10000):
    if c % 100 == 0:
        print("processing %d'th 3-tuple", c)
    candidate = firstprimes[c]
    for prime_pair in prime_pairs:
        good = True
        for prime in prime_pair:
            if candidate < prime:
                candidate_pair = (prime, candidate)
            else:
                candidate_pair = (candidate, prime)
            if candidate_pair not in prime_pairs:
                good = False
                break
        if good:
            prime_3tuples[(*prime_pair, candidate)] = True
print('created %d prime 3-tuples' % len(prime_3tuples))

prime_4tuples = {}
for d in range(1, 10000):
    if d % 100 == 0:
        print("processing %d'th 3-tuple", d)
    candidate = firstprimes[d]
    for prime_3tuple in prime_3tuples:
        good = True
        for prime in prime_3tuple:
            if candidate < prime:
                candidate_pair = (prime, candidate)
            else:
                candidate_pair = (candidate, prime)
            if candidate_pair not in prime_pairs:
                good = False
                break
        if good:
            prime_4tuples[(*prime_3tuple, candidate)] = True
print('created %d prime 4-tuples' % len(prime_4tuples))

prime_5tuples = {}
for e in range(1, 2000000):
    if e % 1000 == 0:
        print("processing %d'th prime with 4tuples", e)
    candidate = firstprimes[e]
    for prime_4tuple in prime_4tuples:
        good = True
        for prime in prime_4tuple:
            if candidate < prime:
                candidate_pair = (prime, candidate)
            else:
                candidate_pair = (candidate, prime)
            if candidate_pair not in prime_pairs:
                good = False
                break
        if good:
            prime_5tuples[(*prime_4tuple, candidate)] = True
            print(prime_4tuple, candidate)
print('created %d prime 5-tuples' % len(prime_5tuples))

print(prime_5tuples.keys())
'''
def test_concatenation_property_indices(indices):
    for x, idx_a in enumerate(indices):
        for y in range(x):
            idx_b = indices[y]
            if (a, b) not in prime_pairs:
                return False
    return True

counter = 0
for indices in index_gen:
    res = test_concatenation_property_indices(indices)
    if res:
        primes_to_test = firstprimes[indices]
        print(primes_to_test)
        print(sum(primes_to_test))
    counter += 1
    if counter >= 2000000:
        break
'''
