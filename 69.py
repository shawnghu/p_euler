'''
Just took this from the solution to 70, which I did first and is strictly harder.
'''
from utils.prime_utils import totient
import numpy as np
import pdb

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}

def is_permutation(num_a, num_b):
    return sorted(str(num_a)) == sorted(str(num_b))

# pdb.set_trace()
maximum = 0
best = None
for i in range(6, 1000000, 6): # quick hack; things much larger than their totient will have a lot of factors, and almost certainly will be divisible by 2 and 3.
    if i % 10000 == 1:
        print(i)
    t = int(totient(i, diprimes))
    if i / t > maximum:
        maximum = i / t
        best = (i, t)
        print(best)
print(best)

