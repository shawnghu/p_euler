from utils.prime_utils import totient
import numpy as np
import pdb

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}

def is_permutation(num_a, num_b):
    return sorted(str(num_a)) == sorted(str(num_b))

# pdb.set_trace()
minimum = 1000000
best = None
for i in range(3, 10000000, 2):
    # 783169, 781396 is a known solution, from an earlier search
    if i % 100000 == 1:
        print(i)
    prime_threshold = 783169 / (783169 - 781396)
    skip = False
    for prime in diprimes:
        if prime > prime_threshold:
            break
        if i % prime == 0:
            skip = True
            break
    if skip:
        continue
    t = int(totient(i, diprimes))
    if is_permutation(i, t):
        if i / t < minimum:
            minimum = i / t
            best = (i, t)
print(best)

