# This is one of those ones that is partially about research ability
# I want to claim that no short amount of time spent thinking independently would come up with an efficient algorithm to solve this problem;
# unless you were already really strong in algebraic number theory.
# The specific term of interest is not just Diophantine equation, but
# specifically Pell's equation. According to Wikipedia, people have been
# studying Pell's equation since at least 400 BC, and admittedly it was solved in 1150 by an Indian mathematician.

# I have not bothered to understand how fundamental solutions to Pell's equation
# arise from a continued fraction expansion of sqrt(D), but Wikipedia says that they do.

# Postmortem: I had to spend most of my debugging time finding the precision error in the continued fraction expansion.
# I took note of this early on, but lost track of it in working memory.
# I was tempted to check stuff like the rational approximation calculation, or the check for the periodic part of the expansion,
# since those are the places where it was likeliest to find a shallow bug.
# But I had already verified those with unit tests, so it was unwise to allocate energy to them early on, and I'm mostly happy with how I avoided focusing on them.


import math
from mpmath import mp

mp.dps = 1000

def continued_fraction_sqrt(D):
    expansion = []
    check = {}
    a = mp.sqrt(D)
    idx = 0
    while True:
        expansion.append(int(a))
        r = a - int(a)
        r_str = str(r)[2:100]
        if r_str in check:
            break
        check[r_str] = idx + 1
        a = 1 / r
        if len(expansion) > 1000:
            print('broke due to long expansion')
            break
        idx += 1
    # ret the "start" of the expansion, and then the periodic part
    return expansion[:check[r_str]], expansion[check[r_str]:]

def rational_approximation(expansion):
    a, b = 1, 0
    for x in reversed(expansion):
        a, b = a * x + b, a
    return a, b

# print(continued_fraction_sqrt(2))
# print(continued_fraction_sqrt(3))
# print(continued_fraction_sqrt(7))
# print(continued_fraction_sqrt(13))

# print(rational_approximation([3, 1, 1, 1, 1, 6, 1, 1, 1, 1]))

biggest = 0
for D in range(2, 1001):
    if math.sqrt(D).is_integer():
        continue
    expansion = continued_fraction_sqrt(D)
    if len(expansion[1]) % 2 == 0:
        app_seq = expansion[0] + expansion[1][:-1] # just based on the fact that these periods are only half as long, I'm pretty sure in order to find the *largest* minimal x we don't even need to check these
    else:
        app_seq = expansion[0] + expansion[1] + expansion[1][:-1]
    x, y = rational_approximation(app_seq)
    if D == 7:
        print(x, y)
    if x > biggest:
        biggest = x
        print(D, x, y)

