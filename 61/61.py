tri_nums = {n * (n + 1) / 2: 1 for n in range(1, 1000)}
square_nums = {n**2: 1 for n in range(1, 1000)}
pent_nums = {n * (3 * n - 1) / 2: 1 for n in range(1, 1000)}
hex_nums = {n * (2 * n - 1): 1 for n in range(1, 1000)}
hept_nums = {n * (5 * n - 3) / 2: 1 for n in range(1, 1000)}
oct_nums = {n * (3 * n - 2): 1 for n in range(1, 1000)}

candidates = [tri_nums, square_nums, pent_nums, hex_nums, hept_nums]
def search(nums, used):
    num = nums[-1]
    for i in range(5):
        if used[i]:
            continue
        for j in range(10, 100):
            next_num = num % 100 * 100 + j
            if next_num in candidates[i]:
                new_nums = nums.copy()
                new_nums.append(next_num)
                new_used = used.copy()
                new_used[i] = True
                if len(new_nums) == 6:
                    if new_nums[0] // 100 == new_nums[5] % 100:
                        return new_nums
                    else:
                        continue
                res = search(new_nums, new_used)
                if res is not None:
                    return res
                else:
                    continue
    return None

for i in range(1000, 10000):
    if i in oct_nums:
        current = i
        used = [False for x in range(5)] # tri thru sept
        res = search([current], used)
        if res is not None:
            print(res)
            print(sum(res))
            break


