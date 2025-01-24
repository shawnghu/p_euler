pentagonal_nums = []
for i in range(1, 100000):
    pentagonal_nums.append(i * (3 * i - 1))

di = {x: True for x in pentagonal_nums}

smallest = 100000000
soln = None
for i in range(99999):
    if (i % 1000) == 0:
        print('i: ', i)
    p1 = pentagonal_nums[i]
    for j in range(i):
        p2 = pentagonal_nums[j]
        # print(p1 - p2) 
        # print (p1 + p2)
        if (p1 - p2) in di and (p1 + p2) in di:
            if (p1 - p2) < smallest:
                smallest = p1 - p2
                soln = (p1, p2)
                print (smallest)

print(soln)
print(smallest)
print(smallest / 2)
