import numpy as np
from utils.prime_utils import totient
import mpmath
import random

import pdb
# print(list(map(lambda x: (3 * x ** 2 - x) % 12, list(range(12)))))
#for char in range(97, 123):
#    print(chr(char))
# firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
# diprimes = {x: True for x in firstprimes}
# pdb.set_trace()
'''
mpmath.dps = 100
a = mpmath.mpf(14)
c = a ** 9
b = (a ** 9) % 55
d = c / 55
print(b)
print(c)
print(d)
'''

counter = 0
double_counter = 0
for x in range(600000):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    double = False
    if a == b:
        double = True
    if double:
        double_counter += 1
        if double_counter >= 3:
            counter += 1
    else:
        double_counter = 0
print(counter)

