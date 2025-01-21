from mpmath import mp
import mpmath


# i somehow convinced myself that this was O(n^2)
# but of course it's actually O(2^n), haha
mp.dps = 200

options = [mp.mpf(1 / (x ** 2)) for x in range(2, 36)]
sum_remaining = [sum(options[i:]) for i in range(len(options))]

def check_sum(options, sum_so_far, idx):
    
    if mpmath.almosteq(sum_so_far, 0.5, abs_eps=mp.mpf(1e-100)):
        return 1
    if idx >= len(options):
        return 0
    if sum_so_far + sum_remaining[idx] < 0.5: # no hope of summing to the target
        return 0
    # if not, we're too small so far
    total = 0
    for potential_add_idx in range(idx, len(options)):
        new_sum = sum_so_far + options[potential_add_idx]
        if new_sum > 0.5:
            continue
        total += check_sum(options, new_sum, potential_add_idx + 1)
    return total

print(check_sum(options, 0, 0))
'''
from sympy.ntheory import factorint
from functools import reduce


# at least do stuff with ints so that the actual arithmetic isn't slow, if it takes a long search
def lcm(l):
    lcm_factors = {}
    for entry in l:
        factors = factorint(entry)
        for factor in factors:
            lcm_factors[factor] = max(lcm_factors.get(factor, 0), factors[factor])
    print(lcm_factors)
    return (reduce(lambda x, y: x * y, [factor ** lcm_factors[factor] for factor in lcm_factors]))

print(lcm([x for x in range(1, 81)]))
'''

# nah, this still isn't good enough, because there are a ton of prime factors
# but this leads me to realize: there's no way that the primes above 40 are showing up in the solution, so we could just ignore them...
# in general, we're not going to have a prime alone without any of its multiples, like if 7 were there but no multiples of 7 were there, we'd be saying
# 1 / 49 + (a bunch of other stuff with no 7s in the denominator) = 1/2
# but of course 1 / 2 - 1 / 49 = 47 / 98, so we'd need some 7s somewhere?

# however, based on the example, the converse is not true; note the xample [2, 3, 4, 6, 7, 8, 10, 20, 28, 35, 36, 45], which manages to get away
# with having a 10, 20, 35, and 45 without having a 5

# observe for starters that 1 / 100 + 1 / 400 = 1 / 80, which still has a factor of 5 in it...
# 1 / 100 + 1 / 400 + 1 / 1225 + 1 / 2025 = 877 / 63504, somehow? and that factorizes to 2^4 * 3^4 * 7^2
# basically, when you find a common denominator for all the multiples of a prime, you need the numerators to sum to something which is divisible by p^2


