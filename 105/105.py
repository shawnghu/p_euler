import itertools
import math
import pdb
def search_matching_sums(l):
    sums_seen = {}
    for combination_size in range(1, len(l) + 1):
    # for combination_size in range(1, math.floor(len(l) / 2) + 1):
        for combination in itertools.combinations(l, combination_size):
            s = sum(combination)
            if s in sums_seen:
                print("search_matching_sums failed on ", l, "with sums equal for: ", combination, ", ", sums_seen[s])
                return False
            sums_seen[s] = combination
    return True

def search_matching_sums_broken(l):
    sums_seen = {}
    for combination_size in range(1, math.floor(len(l) / 2) + 1): # I mistakenly assumed that subsets that sum to the same number must have the same size, here. That caused me to drop one.
        for combination in itertools.combinations(l, combination_size):
            s = sum(combination)
            if s in sums_seen:
                # print("search_matching_sums failed on ", l, "with sums equal for: ", combination, ", ", sums_seen[s])
                return False
            sums_seen[s] = combination
    return True

def search_size_condition(l):
    # l = sorted(l)
    l.sort()
    # print(l)
    for i in range(2, len(l)):
        # print(l[:i])
        # print(l[-i + 1:])
        if sum(l[:i]) < sum(l[-i + 1:]):
            # print("search_size_condition failed on ", l, "with sublists: ", l[:i], "with sum: ", sum(l[:i]), ", ", l[-i + 1:], "with sum: ", sum(l[-i + 1:]))
            return False
    return True

# pdb.set_trace()
# print(search_matching_sums([157,150,164,119,79,159,161,139,158]))
print(search_matching_sums([68, 46, 64, 33, 60, 58, 65]))
# print(search_size_condition([81,88,75,42,87,84,86,65]))
# print(search_size_condition([1, 2, 3, 4]))
sys.exit()

total = 0
with open("sets.txt", "r") as f:
    for line in f.readlines():
        nums = line.strip().split(',')
        nums = [int(num) for num in nums]
        # pdb.set_trace()
        if search_matching_sums(nums) != search_matching_sums_broken(nums):
            print(nums)
        # if search_size_condition(nums): #and search_size_condition(nums):
            print(nums)
            total += sum(nums)
            # print(total)
print(total)
