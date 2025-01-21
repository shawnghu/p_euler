from sympy.ntheory import factorint
import itertools
import functools

def sum_proper_divisors(n):
    factors = factorint(n)
    power_lists = [
        [prime ** i for i in range(power + 1)]
        for prime, power in factors.items()
    ]
    combinations_of_powers = itertools.product(*power_lists)
    factors = [functools.reduce(lambda x, y: x * y, combination) for combination in combinations_of_powers]
    return sum(factors) - n

'''
def proper_divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
'''

# since the sum_proper_divisors function is adequately fast,
# the problem is now pretty easy...
n_to_sdn = {}
handled = {}
for i in range(2, 1000000):
    n_to_sdn[i] = sum_proper_divisors(i)

longest_cycle = 0
for n in range(2, 1000000):
    if n in handled:
        continue
    cycle = []
    k = n
    while k not in handled and k not in cycle:
        # handled[k] = True # this doesn't work, since you can enter a cycle from outside the cycle
        cycle.append(k)
        k = n_to_sdn[k]
        if k == 1 or k > 1000000:
            for i in cycle:
                handled[i] = True
            break
    if k == n:
        # then this was a cycle, starting with n
        if len(cycle) > longest_cycle:
            longest_cycle = len(cycle)
            print(cycle) # a nice side effect is due to the handling logic, each cycle is only printed once, with the smallest element first
    # if k != n, this may have contained a cycle, so we don't mark handled
'''
for i in range(2, 100):
    print(i, sum_proper_divisors(i))
    '''
