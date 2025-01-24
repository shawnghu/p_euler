from utils.prime_generator import naivePrimeGenerator
import itertools
import math
import sys

primegen = naivePrimeGenerator()
firstprimes = list(itertools.islice(primegen, 78700))
diprimes = {x: True for x in firstprimes}

# 0th index corresponds to 1's place, 1th index corresponds to 10s, etc.
def replace_digits(num, indices, new_digit):
    for idx in indices:
        num -= (num % 10 ** (idx + 1) - num % 10 ** (idx))
        num += new_digit * 10 ** (idx)
    return num

def try_indices(num, indices, length_of_prime):
    counter = 0
    for i in range(10):
        if length_of_prime - 1 in indices and i == 0: # bodge to deal with the fact that we don't like to replace the first digit with 0
            continue
        # print(replace_digits(num, indices, i))
        if replace_digits(num, indices, i) in diprimes:
            counter += 1
    if counter >= 8:
        print(num, indices)

def powerset(iterable):
	"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	s = list(iterable)
	return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def try_find_family(prime):
    length_of_prime = math.floor(math.log(prime, 10)) + 1 # technically doesn't work for all numbers possibly due to precision problems, but this shouldn't arise for primes
    combinations = powerset(range(1, length_of_prime))
    for indices in combinations:
        if len(indices) > 0:
            # print(indices)
            try_indices(prime, indices, length_of_prime)
	
# print(list(powerset([1, 2, 3])))
# sys.exit()
# try_indices(56003, [1, 2])
for prime in firstprimes:
    try_find_family(prime)
    

# print(replace_digits(111111, [True, True, True, True, True], 2))
