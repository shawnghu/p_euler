import math

def nCr(n, r):
    return (math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

counter = 0
for i in range(101):
    print(i)
    for j in range(i + 1):
        if nCr(i, j) > 1000000:
            counter += 1
print(counter)
