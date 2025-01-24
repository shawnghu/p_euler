# Pretty sure we can just brute force this one.

import itertools

raw_nums = list(range(1, 21))
scores = list(itertools.product('SDT', raw_nums)) + [('S', 25), ('D', 25)]
doubles = list(itertools.product('D', raw_nums)) + [('D', 25)]

def is_double(score):
    return score[0] == 'D'

def get_value(score):
    if score[0] == 'S':
        return score[1]
    if score[0] == 'D':
        return score[1] * 2
    if score[0] == 'T':
        return score[1] * 3

def get_value_of_scores(tup):
    total = 0
    for score in tup:
        total += get_value(score)
    return total

total = 21 # this is all the single dart doubles
for score in scores:
    for double in doubles:
        if get_value_of_scores((score, double)) < 100:
            print(score, double)
            total += 1

for combination in itertools.combinations_with_replacement(scores, 2):
    for double in doubles:
        if get_value_of_scores(combination) + get_value(double) < 100:
            total += 1
print(total)
