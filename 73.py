import numpy as np
from utils.prime_utils import factorize

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}

def is_coprime(numerator, denominator, primes):
    if denominator in primes:
        return True
    numfactors = factorize(numerator, primes)
    denfactors = factorize(denominator, primes)
    for factor in numfactors:
        if factor in denfactors:
            return False
    return True



# fracs = {}
counter = 0
for denom in range(1, 12001):
    if denom % 1000 == 0:
        print(denom)
    for numerator in range(int(denom / 3), int(denom / 2 + 2)):
        if numerator / denom <= 1/3:
            continue
        if numerator / denom >= 1/2:
            continue
        if is_coprime(numerator, denom, diprimes):
            counter += 1
print(counter)

