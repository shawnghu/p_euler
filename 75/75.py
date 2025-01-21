import sys

m = 2
ways = {}
ab = {}
print
while True:
    if m ** 2 >= 1500000:
        break
    for n in range(m % 2 + 1, m, 2): # m - n must be odd
        if m ** 2 + n ** 2 >= 750000:
            break
        a = m ** 2 - n ** 2
        b = 2 * m * n
        if b < a:
            a, b = b, a
        if (a, b) in ab:
            continue
        c = m ** 2 + n ** 2
        if a + b + c <= 1500000:
            for k in range(1, 1500000 // (a + b + c) + 1):
                ab[(k * a, k * b)] = True
                ways[k * (a + b + c)] = ways.get(k * (a + b + c), 0) + 1
    m += 1
    if m % 100 == 0:
        print(m)

print(sum(1 for way in ways if ways[way] == 1))

