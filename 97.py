import math
def compute_exp(base, exp, modulus=0):
    effective_base = 1
    current_exp = base
    exps = [current_exp]
    while True:
        effective_base *= 2
        if effective_base > current_exp:
            break
        current_exp = (current_exp * current_exp) % modulus
        exps.append(current_exp)
    total = 1
    while exp > 0:
        a = math.floor(math.log(exp, 2))
        total = (total * exps[a]) % modulus
        exp -= (2 ** a)
    return total

a = (compute_exp(2, 7830457, 1e10))
print(a)
print(a * 28433 + 1)






