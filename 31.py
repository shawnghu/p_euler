COINS = [1, 2, 5, 10, 20, 50, 100, 200]
'''
from functools import reduce

class PartialSolution(object):

    def __init__(self, other=None):
        if other is not None:
            self.remainder = other.remainder
            self.counts = list(other.counts)
        else:
            self.remainder = 0
            self.counts = [0, 0, 0, 0, 0, 0, 0, 0]

    def increment_at_idx(idx):
        self.counts[idx] += 1


    def __hash__(self):
        return hash(reduce(lambda x, y: x * y, self.counts))

    def __eq__(self, other):
        if self.remainder != other.remainder:
            return False
        for idx, count in enumerate(self.counts):
            if count != other.counts[idx]:
                return False
        return True
'''


cache = {}

def count_make(remainder, enc_coins):
    if remainder < 0:
        return 0
    # print('Testing partial solution with remainder: ' +  str(partial_solution.remainder) + ', counts: ' + str(partial_solution.counts))
    cache[(remainder, enc_coins)] = True
    if remainder == 0:
        return 1
    total = 0
    for idx, coin in enumerate(COINS):
        new_remainder = remainder - coin
        new_enc_coins = enc_coins + 2 ** (idx * 8)
        if (new_remainder, new_enc_coins) not in cache:
            total += count_make(new_remainder, new_enc_coins)
    return total

# base = PartialSolution()
# base.remainder = 200
print(count_make(200, 0))
