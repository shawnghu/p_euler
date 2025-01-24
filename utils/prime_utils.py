import functools
import math
import bisect

# checking against even the first 10 million primes, cached, isn't enough, so check directly via trial division
def isprime(num, prime_cache={}, max_value_in_cache=179400000):
    # print ('primality testing: %d' % num)
    if num < max_value_in_cache:
        return num in prime_cache
    sqrt = num ** 0.5
    for x in prime_cache: # this relies on the keys being in order, which seems like they are for a standard list comprehension
        if num % x == 0:
            return False
        if x > sqrt:
            break
    else:
        raise Exception("you forgot to implement the behavior for what happens if there isn't already a prime cache. sieve?")
    return True

def is_prime_by_trial_division(num, prime_list):
    sqrt = math.floor(math.sqrt(num))
    max_prime_idx = bisect.bisect(prime_list, sqrt)
    for prime in prime_list[:max_prime_idx]:
        if num % prime == 0:
            return False
    return True

    
def factorize(num, primes):
    factors = []
    while True:
        if num in primes:
            factors.append(num)
            return factors
        for prime in primes:
            if prime > num ** 0.5:
                # the number is prime
                factors.append(num)
                return factors
            if num % prime == 0:
                factors.append(prime)
                num /= prime
                break # out of the for loop, not out of the while loop
    return factors

def totient(num, primes):
    factors = set(factorize(num, primes))
    for factor in factors:
        num *= factor - 1
        num /= factor
    return num
