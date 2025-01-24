import numpy as np
import pdb
from utils.prime_utils import isprime

firstprimes = np.load('utils/first_10million_primes.npy')
diprimes = {x: True for x in firstprimes}

# print(firstprimes[-1])

#sys.exit()

# pdb.set_trace()



side_length = 1
first_diagonal_primes = []
second_diagonal_primes = []

first_diagonal_value = 1
second_diagonal_value = 1
first_diagonal_increment = 2
second_diagonal_increment = 4

while True:
    side_length += 2
    first_diagonal_value += first_diagonal_increment
    #print(first_diagonal_value)
    if isprime(first_diagonal_value, diprimes):
        first_diagonal_primes.append(first_diagonal_value)
    first_diagonal_increment += 2

    first_diagonal_value += first_diagonal_increment
    #print(first_diagonal_value)
    if isprime(first_diagonal_value, diprimes):
        first_diagonal_primes.append(first_diagonal_value)
    first_diagonal_increment += 2

    second_diagonal_value += second_diagonal_increment
    if isprime(second_diagonal_value, diprimes):
        second_diagonal_primes.append(second_diagonal_value)
    second_diagonal_value += second_diagonal_increment
    if isprime(second_diagonal_value, diprimes):
        second_diagonal_primes.append(second_diagonal_value)
    second_diagonal_increment += 4

    if (len(first_diagonal_primes) + len(second_diagonal_primes) * 1.0) / (2 * side_length - 1) < 0.1:
        print(first_diagonal_primes)
        print(second_diagonal_primes)
        print(len(first_diagonal_primes))
        print(len(second_diagonal_primes)) #179399237, 179424673

        print(side_length)
        break
