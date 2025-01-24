'''
Another overrated problem. Conceptually I think the only trick is to realize that there aren't very many squares/cubes/fourth powers to iterate over,
then it's just a brute force which doesn't even need to be optimized.
2 / 3 of this script is just cutting arrays down to optimal size to slightly speed up the brute force.
I'm a little frustrated, though, I did spend several minutes ironing out completely careless bugs.
'''
import numpy as np
import pdb

firstprimes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
i = 0
while True:
    i += 1
    if firstprimes[i] > 50000000 ** 0.5:
        break
firstprimes = firstprimes[:i]

squares = firstprimes ** 2
# disquares = {x: True for x in squares}

cubes = firstprimes ** 3
i = 0
while True:
    i += 1
    if cubes[i] > 50000000:
        break
cubes = cubes[:i]
#dicubes = {x: True for x in cubes}

fourthps = firstprimes ** 4
i = 0
while True:
    i += 1
    if fourthps[i] > 50000000:
        break
fourthps = fourthps[:i]
#disquares = {x: True for x in fourthps}

sums = []
# pdb.set_trace()
print(len(squares))
for idx, square in enumerate(squares):
    for cube in cubes:
        for fourthp in fourthps:
            s = square + cube + fourthp
            if s > 50000000:
                break
            sums.append(square + cube + fourthp)
print(len(set(sums)))
