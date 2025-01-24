import numpy as np
import pdb
import math

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
diprimes = {x: True for x in firstprimes}

visited = {}
fac_digits = {n: math.factorial(n) for n in range(10)}

def factorialize(n):
    total = 0
    while n > 0:
        total += fac_digits[n % 10]
        n //= 10
    return total

def try_cycle(num):
    num_to_idx = {}
    index = 0
    while True:
        num_to_idx[num] = index
        num = factorialize(num)
        visited[num] = True
        index += 1
        if num in num_to_idx:
            if index == 60:
                return True
            else:
                return False


counter = 0
for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    if i in visited:
        continue
    if try_cycle(i):
        counter += 1
print(counter)

