# this one is going to be annoying because of the way the constraints have to be encoded
# strong assumption: the only awy to get a 16 digit string is going to be if the 10 is on the outside.

# 10! is only 3628800, so we can just try all of them, I think.
# We can break down a few symmetries by assuming that 10 is the "first" entry.
# There is at least one other symmetry ot take advantage of, which is that the smallest number has to come "first", but I don't want to think about that.

import itertools

def is_magic(perm):
    sum = 10 + perm[4] + perm[5]
    if sum != perm[0] + perm[5] + perm[6]:
        return False
    if sum != perm[1] + perm[6] + perm[7]:
        return False
    if sum != perm[2] + perm[7] + perm[8]:
        return False
    if sum != perm[3] + perm[8] + perm[4]:
        return False
    return True

def find_string(perm):
    if min(perm[:4]) == perm[0]:
        return [perm[0], perm[5], perm[6], perm[1], perm[6], perm[7], perm[2], perm[7], perm[8], perm[3], perm[8], perm[4], 10, perm[4], perm[5]]
    if min(perm[:4]) == perm[1]:
        return [perm[1], perm[6], perm[7], perm[2], perm[7], perm[8], perm[3], perm[8], perm[4], 10, perm[4], perm[5], perm[0], perm[5], perm[6]]
    if min(perm[:4]) == perm[2]:
        return [perm[2], perm[7], perm[8], perm[3], perm[8], perm[4], 10, perm[4], perm[5], perm[0], perm[5], perm[6], perm[1], perm[6], perm[7]]
    if min(perm[:4]) == perm[3]:
        return [perm[3], perm[8], perm[4], 10, perm[4], perm[5], perm[0], perm[5], perm[6], perm[1], perm[6], perm[7], perm[2], perm[7], perm[8]]
    

for perm in itertools.permutations(range(1, 10)):
    if is_magic(perm):
        print(find_string(perm))
        print(int("".join(map(str, find_string(perm))))) 
