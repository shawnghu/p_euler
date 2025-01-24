# I'm going to attempt to compute rational approximations to the square root of 1/2.
# I'm not sure a priori if this should give us the smallest values over 1 billion, but it would be cool if it did.
# Update: No, it didn't work, obviously. I got 543339720 / 768398401, which gets us 1/2 to 9 decimal places when you plug it into the problem.

import mpmath
from mpmath import mp

'''
mpmath.dps = 400
sequence = []
n = mp.sqrt(0.5)
for i in range(200):
    n = 1 / n
    sequence.append(mpmath.floor(n))
    print(mpmath.nstr(n, 12))
    n = mpmath.frac(n)

print(sequence)
'''


sequence = [2 for x in range(100)]
sequence[0] = 1

def compute_partial(n):
    denominator = mpmath.mpf(sequence[n])
    numerator = mpmath.mpf(1)
    for i in range(n - 1, -1, -1):
        numerator = sequence[i] * denominator + numerator
        numerator, denominator = denominator, numerator
    return numerator, denominator

mpmath.dps = 100
num, den = (compute_partial(23))
print(num, den)

print(num * (num - 1) * 2)
print(den * (den - 1))
