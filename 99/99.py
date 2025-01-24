import math
with open("base_exp.txt", "r") as f:
    best_index = -1
    biggest = 0
    idx = 0
    for line in f.readlines():
        base, exp = line.strip().split(',')
        base, exp = int(base), int(exp)
        val = exp * math.log(base) # the base of the log of course doesn't matter
        if val > biggest:
            biggest = val
            best_index = idx
        idx += 1
print(best_index)
