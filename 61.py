
poly_nums = {}
def add_nums(poly_idx, lambda_formula)
    for i in range(1000):
        num = lambda_formula(i)
        if num > 10000:
            break
        if num < 1000:
            continue
        nums[num] = poly_idx




