# there are only 28 possibilities for each cube, so i think you can just brute force it
# why is this one so infrequently solved?

import itertools

squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

def digit_on_die(digit, die):
    # return digit in die
    if digit == '9' or digit == '6':
        return '9' in die or '6' in die
    else:
        return digit in die

def can_do_the_thing(die_a, die_b):
    for square in squares:
        digit_1 = square[0]
        digit_2 = square[1]
        can_make_this_square = False
        if digit_on_die(digit_1, die_a) and digit_on_die(digit_2, die_b):
            can_make_this_square = True
        if digit_on_die(digit_2, die_a) and digit_on_die(digit_1, die_b):
            can_make_this_square = True
        if not can_make_this_square:
            return False
    return True
            
        
# print(can_do_the_thing(('0', '5', '6', '7', '8', '9'), ('1', '2', '3', '4', '6', '7')))
dice = list(itertools.combinations('012345678', 5))
dice = [x for x in dice if '6' in x]
dice += list(itertools.combinations('012345678', 6))
counter = 0

# the problem doesn't specify with replacement or not, but that turns out to be moot because no set of six digits can do the task
for (die_a, die_b) in itertools.combinations(dice, 2):
    if can_do_the_thing(die_a, die_b):
        to_add = 1
        if '6' in die_a and len(die_a) == 6:
            to_add *= 2
        if '6' in die_b and len(die_b) == 6:
            to_add *= 2
        counter += to_add
print(counter)

# fuck: this only counts ones that don't contain 6 and 9 on them
# you need to also look for combinations of 5 things that contain 6 that satisfy

