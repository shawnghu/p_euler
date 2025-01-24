'''
Let's see how far the brute force method goes.

Let k be half the length of the side that doesn't match the other two.
Then the other two sides have length 2k - 1 or 2k + 1, and the total perimeter is 6k - 2 or 6k + 2.
So k only needs to go up to 166,666,667.

We need to check that the difference in squares is another square.
'''

import numpy as np
import mpmath

'''
# Running the numpy version of this is substantially faster, but I'm using a shitty minimum stock Dell XPS 15 and it OOMs if i try to increase the precision.
ks = np.arange(4, 166666667, 2)
print('a')
threeksquareds = 3 * (ks ** 2)
fourks = 4 * ks
print('b')
longers = np.sqrt(threeksquareds + fourks + 1)
shorters = np.sqrt(threeksquareds - fourks + 1)
print('c')

total = 0
for idx, k in enumerate(ks):
    if idx % 10000000 == 0:
        print(idx)
    if longers[idx].is_integer():
        total += k * 6 + 2
    if shorters[idx].is_integer():
        total += k * 6 - 2
print(total)

'''

# This is a naive check to see if something can be a square by checking its value modulo a good number.
# In this way we can skip calculating the square for 97+% of the numbers (and subsequently the square root).
# This solution takes about 30 seconds to compute the good moduluses with a naive search, and another 120 seconds for the actual calculation on a Dell XPS.
# A qualitatively faster algorithm may take advantage of stuff like the Legendre/Jacobi symbol + quadratic reciprocity stuff for the squares after they are calculated.
# I also didn't do a lot of work to determine what the best possible modulus is. Clearly, I just slapped in the product of a bunch of primes.
# Also, I wish there were an easier way to increase the precision; mpf seems to be overkill and does remove the parallelism of numpy.
# I guess we could custom-roll some arithmetic operations because we only need twice the precision of a double, but I don't want to do that with my life.
good_residues_longers = {}
good_residues_shorters = {}
MODULUS = 9 * 25 * 49 * 121 * 13
squares = set()
for i in range(MODULUS):
    squares.add((i * i) % MODULUS)

for i in range(MODULUS):
    if (3 * i * i + 4 * i + 1) % MODULUS in squares:
        good_residues_longers[i] = True
    if (3 * i * i - 4 * i + 1) % MODULUS in squares:
        good_residues_shorters[i] = True
        
print('done calculating residues')

mpmath.dps = 26
total = mpmath.mpf(0)
# for i in range(3, 166666667):
for i in range(3, 166666667):
    if i % 10000000 == 0:
        print(i)
    if i % MODULUS not in good_residues_longers:
        continue
    i = mpmath.mpf(i)
    if mpmath.isint(mpmath.sqrt(3 * (i ** 2) + (4 * i) + 1)):
        total += i * 6 + 2

for i in range(3, 166666667):
    if i % 10000000 == 0:
        print(i)
    if i % MODULUS not in good_residues_shorters:
        continue
    i = mpmath.mpf(i)
    if mpmath.isint(mpmath.sqrt(3 * (i ** 2) - (4 * i) + 1)):
        total += i * 6 - 2

print(total)
