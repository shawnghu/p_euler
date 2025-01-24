import math
def count_rectangles(m, n):
    '''
    total = 0
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            total += x * y
    '''
    total = m * (m + 1) / 2 * n * (n + 1) / 2
    return total

diff = 1000000
best = None
for m in range(1414):
    for n in range(m):
        subs = count_rectangles(m, n)
        if math.fabs(subs - 2000000) < diff:
            diff = math.fabs(subs - 2000000)
            best = (m, n)
print(best)
