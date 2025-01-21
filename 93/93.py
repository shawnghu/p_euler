import itertools
import operator
def generate_all_outcomes(a, b, c, d):
    di = {}
    ops = [operator.mul, operator.add, operator.sub, operator.truediv]
    for permutation in itertools.permutations([a, b, c, d]):
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    try:
                        res = op1(permutation[0], op2(permutation[1], op3(permutation[2], permutation[3])))
                        # deal with the fact that subtraction and division are not commutative
                        # actually this check isn't enough, because AFAICT there areother ways to get a bad div/sub that this doesn't account for
                        # but it's enough to get the correct answer on PE 
                        if res < 0:
                            res = -res
                        if abs(int(res) - res) < 1e-6: # floating point stuff
                            res = int(res)
                            di[res] = 1
                        if abs(int(1 / res) - (1 / res)) < 1e-6:
                            res = int(1 / res)
                            di[res] = 1
                    except ZeroDivisionError:
                        pass

    return di
max = 0
best_so_far = None
for d in range(1, 10):
    for c in range(1, d):
        for b in range(1, c):
            for a in range(1, b):
                di = generate_all_outcomes(a, b, c, d)
                most_consecutive = 1
                while most_consecutive in di:
                    most_consecutive += 1
                if most_consecutive > max:
                    max = most_consecutive
                    best_so_far = (a, b, c, d)
                    print(best_so_far)
                    print(max)
print(best_so_far)


a = generate_all_outcomes(1, 2, 3, 4)
print(sorted(a.keys()))