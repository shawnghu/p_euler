from utils.prime_utils import isprime
import numpy as np
import pdb

def index_generator():
    for total in range(1000):
        for a in range(total):
            for b in range(a):
                if b > total - a:
                    break
                for c in range(b):
                    if c > total - a - b:
                        break
                    for d in range(c):
                        if d > total - a - b - c:
                            break
                        for e in range(d):
                            if a + b + c + d + e == total:
                                yield (a, b, c, d, e)

index_gen = index_generator()
'''
for i in range(100):
    print(next(indices))
'''  

firstprimes = np.load('utils/first_10million_primes.npy')
#pdb.set_trace()
diprimes = {x: True for x in firstprimes}

def test_concatenation_property(prime_set):
    # all the primes in this set have to have the same value mod 3, or else concatenating two will yield something divisible by 3
    pmod3 = prime_set[0] % 3
    for prime in prime_set:
        if prime == 3:
            continue
        if prime % 3 != pmod3:
            return False

    for prime_a in prime_set:
        for prime_b in prime_set:
            if prime_a == prime_b:
                continue
            if not isprime(int(str(prime_a) + str(prime_b)), diprimes):
                return False
            if not isprime(int(str(prime_b) + str(prime_a)), diprimes):
                return False
    return True

# print(test_concatenation_property((3, 7, 109, 673)))

counter = 0
for indices in index_gen:
    if 1 in indices:
        continue # hack, skip 5 also
    primes_to_test = [firstprimes[idx + 1] for idx in indices] # skip 2, 'cause obviously that's going to cause problems
    res = test_concatenation_property(primes_to_test)
    if res:
        print(primes_to_test)
        print(sum(primes_to_test))
    counter += 1
    if counter >= 10000000:
        break
