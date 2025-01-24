from utils.prime_utils import totient
import numpy as np

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}


total = 0
for x in range(2, 1000001):
    total += totient(x, diprimes)
print(total)

