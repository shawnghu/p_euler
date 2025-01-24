import itertools
import more_itertools

it = '3333x'
# print(list(itertools.permutations(it)))
print(list(more_itertools.distinct_permutations(it)))
