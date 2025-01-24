import collections
import functools

seeds = {}
def seed_gen():
    queue = collections.deque()
    queue.append([2, 2])
    while len(queue) > 0:
        new_seed = queue.popleft()
        if tuple(new_seed) in seeds:
           continue
        if functools.reduce(lambda x, y: x * y, new_seed) > 100000:
            continue
        seeds[tuple(new_seed)] = True
        yield new_seed
        queue.append(new_seed + [2])
        last_value = None
        for idx, value in enumerate(new_seed):
            if value != last_value:
                to_add = new_seed.copy()
                to_add[idx] += 1
                queue.append(to_add)
            last_value = value

seed_generator = seed_gen()
counter = 0
minimal_numbers = [100000 for x in range(12001)]
for indices in seed_generator:
    product = functools.reduce(lambda x, y: x * y, indices)
    s = functools.reduce(lambda x, y: x + y, indices)
    k = product - s + len(indices)
    # no easy way to verify we got the minimal number for k
    if k <= 12000:
        if product < minimal_numbers[k]:
            minimal_numbers[k] = product
    counter += 1
    if counter % 50000 == 0:
        print(counter)
# print(sorted(ks))

# for i in range(12000): # no positives, so we covered the whole range
#    if i not in ks:
#        print(i)

print(sum(list(set(minimal_numbers[2:]))))
