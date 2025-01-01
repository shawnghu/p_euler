
# wrote this on a different laptop without my libs, so just a quick prime checker
# doesn't need check for < 2 due to the nature of the problem
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# spoke numbers are the numbers on the "spokes" of the hexagonal grid
# i.e, those that are in a straight line from the center of the grid
# i singled these out because they have different 
'''
def generate_spoke_numbers_and_diffs_up_to(n):
    x = 2
    to_add = 1
    while True:
        diffs_from_neighbors = []
        diff_from_beneath = 6 * (to_add - 1)
        diff_from_above = diff_from_beneath + 6
        for i in range(6):
            x += to_add
            diff_from_beneath += 1
            diff_from_above += 1
            diffs_from_neighbors = [diff_from_beneath, diff_from_above - 1, diff_from_above, diff_from_above + 1]
            if i == 5:
                # you have one more neighbor to the upper right due to the way we go to a new "layer"
                top_right_neighbor = x + 6 * (to_add + 1) + 6 * (to_add + 2) - 1
                diffs_from_neighbors.append(top_right_neighbor - x)
            layer_number = to_add + 1 if i == 5 else to_add
            yield (x, i, layer_number, diffs_from_neighbors)
        to_add += 1
        if x > n:
            break
'''
            
# from evidence we observe that when spoke i != 5, the neighbors are always n, n+5, n+6, n+7
# in that case, it's not possible for 3 of these to be prime, since
# obvious n+5, n+6, n+7 are not all prime because they have different parities,
# so n would have to be prime, but then n+5, n+7 would both be even.


# there are a small number of these, and calculating them explicitly is very fast
# the strategy in this problem is to single these out, but then characterize the neighbor-behavior of the non-spoke numbers
# to make this calculation easy.
'''
for x, i, _, diffs in generate_spoke_numbers_and_diffs_up_to(1000):
    print(x, i, diffs)
'''
'''
for x, i, to_add, neighbors in generate_spoke_numbers_and_diffs_up_to(50):
    print(x, i, to_add, neighbors)
'''
'''
pd3idx = 0
a = generate_spoke_numbers_and_diffs_up_to(10 ** 9)
layer_number = 0
next_spoke_number = None
while True:
    if next_spoke_number is not None:
        layer_number = next_layer_number
    next_spoke_number, next_spoke_i, next_layer_number, next_diffs_from_neighbors =  next(a)
    if next_spoke_number == 8:
        break
for i in range(2, 10 ** 9):
    if i == next_spoke_number:
        diffs_from_neighbors = next_diffs_from_neighbors
        layer_number = next_layer_number
        next_spoke_number, next_spoke_i, next_layer_number, next_diffs_from_neighbors = next(a)
    else:
        # most numbers are in this category: the non-spoke numbers
        # one neighbor is i - 1, and another is i + 1
        
        # there are four neighbors, which i'll call "lower beneath," "upper beneath," "lower above," and "upper above"
        # the nomenclature is that "lower" means "towards the center of the grid"
        diff_from_lower_beneath = (layer_number - 1) * 6 + 1 + next_spoke_i
        diff_from_upper_beneath = diff_from_lower_beneath - 1
        diff_from_upper_above = ((layer_number) * 6 + 1 + next_spoke_i)
        diff_from_lower_above = diff_from_upper_above - 1
        # except this special case: this is the last number in the layer, so its neighbor to the bottom left
        # # (in absolute terms) is the first number in the previous layer
        if next_spoke_i == 5 and i == next_spoke_number - 1:
            upper_beneath = i + 1 - (layer_number + layer_number - 1) * 6
            diff_from_upper_beneath = i - upper_beneath
            pass
        diffs_from_neighbors = [diff_from_lower_beneath, diff_from_upper_beneath, diff_from_upper_above, diff_from_lower_above]
    PD = 0
    for diff in diffs_from_neighbors:
        if is_prime(diff):
            PD += 1
    if PD == 3:
        pd3idx += 1
        if pd3idx % 50 == 0:
            print(pd3idx)
        if pd3idx == 1999 or pd3idx == 2000 or pd3idx == 2001:
            print(i)
        if pd3idx == 2001:
            break

# the above program is correct, but will take probably several minutes to several hours to run
# since the above is correct, at least we have characterized the neighbor behavior of all the numbers
# i mistakenly thought 17 was a pd = 3 number, because i misread the problem statement
# in reality, i expect that non-spoke numbers cannot be pd = 3, and if i prove that, i can skip all of them...
'''

# i had this proof earlier but mistakenly thought it did not hold:
# non-spoke numbers cannot be pd = 3, except for the exception named above.
# the two neighbors have diffs of 1,
# and the other neighbors come in pairs, of which for each pair, only one can be prime, since they have
# different parities.


# given all of this, we only need to search the first and last number in each layer.

def generate_candidate_numbers_up_to(n):
    yield 2
    yield 7
    parity = True
    layer_number = 1
    while True:
        if parity:
            # do first number in layer
            x = layer_number * (layer_number + 1) * 3 + 2
            yield x
            parity = False
            continue
        else:
            # do last number in layer
            x = (layer_number + 1) * (layer_number + 2) * 3 + 1
            yield x
            parity = True
            layer_number += 1
        if x > n:
            break
candidate_numbers = list(generate_candidate_numbers_up_to(5 * 10 ** 10))
# print(candidate_numbers)

'''
def generate_candidate_numbers_and_diffs_up_to(n):
    parity = True

    while True:
        if parity:
            # do first number in layer
            parity = False
            continue
        else:
            # do last number in layer
            parity = True
'''

counter = 0
for idx, x in enumerate(candidate_numbers):
    if idx % 2 == 0:
        if idx + 4 >= len(candidate_numbers):
            continue
        # a first number in a layer
        neighbors = [candidate_numbers[idx + 2] - 1, candidate_numbers[idx + 2] + 1, candidate_numbers[idx + 4] - 1]
    else:
        if idx - 3 < 0 or idx + 3 >= len(candidate_numbers):
            continue
        # a last number in a layer
        neighbors = [candidate_numbers[idx - 3], candidate_numbers[idx - 1], candidate_numbers[idx + 3] - 2]
    diffs_from_neighbors = [abs(x - neighbor) for neighbor in neighbors]
    PD = 0
    for diff in diffs_from_neighbors:
        if is_prime(diff):
            PD += 1
    if PD == 3:
        counter += 1
        print(counter, x)
        if counter > 12:
            break
        if counter % 50 == 0:
            print(counter)
        # need 1999, since the whole thing is off by 1 since our method doesn't work for n=1, which is a PD = 3 number
        if counter == 1999 or counter == 2000 or counter == 2001: 
            print(x)
        if counter == 2001:
            break
