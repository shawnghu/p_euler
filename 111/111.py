# Logically speaking, the question breaks down to:
# For each digit d:
# What is M(10, d) (how many times can you get the digit to repeat)?
# Given what M(10, d) is, what are all the primes that fit that criteria? then sum them
# This can't be answered super-super directly because we cannot generate a cache of all the ten digit primes
# (there are so many that it takes too much memory, notwithstanding time)
import math
import more_itertools
from utils.prime_utils import is_prime_by_trial_division
from utils.prime_generator import naiveSieveOfEratosthenesMod6
import pdb

prime_list = naiveSieveOfEratosthenesMod6(math.floor(math.sqrt(1e10)))

def replace_x_with_incrementing_numbers(s):
    indices = []
    for idx, entry in enumerate(s):
        if entry == 'x':
            indices.append(idx)
            s[idx] = 0
    yield s
    while True:
        broke = False
        for i in indices:
            if s[i] != 9:
                s[i] += 1
                yield s.copy()
                broke = True
                break
            else:
                s[i] = 0
                continue
        if not broke:
            break

# The trick to this one is that there will amost certainly be a prime for m = 9 or maybe m = 8, so the search space is not nearly as large as it looks.
# For m = 9, there are about 100 numbers to look at; for m = 8, only about ten thousand. That means you actually only have to do at most 100,000 trial division primality checks.
# And the rest of this code is pretty ugly and have a lot of overhead, but the high order amount of work is really good so it doesn't matter.
def find_s(digit):
    for m in range(9, 5, -1):
        primes = []
        for permutation in more_itertools.distinct_permutations(str(digit) * m + str('x') * (10 - m)):
            if permutation[0] == '0':
                continue
            for prime_candidate in replace_x_with_incrementing_numbers(list(permutation)):
                if prime_candidate[0] == 0:
                    continue
                prime_candidate = int(''.join([str(x) for x in prime_candidate]))
                if is_prime_by_trial_division(prime_candidate, prime_list):
                    primes.append(prime_candidate)
                    print('found a prime ', prime_candidate, 'with m = ', m)
        if len(primes) > 0:
            return sum(primes)

total = sum(find_s(i) for i in range(10))
print(total)
# print(list(replace_x_with_incrementing_numbers(['9', 'x', '4', 'x'])))
# print(len(list(replace_x_with_incrementing_numbers(['9', 'x', '4', 'x']))))
