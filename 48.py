def findlasttendigits(base, exp):
    total = 1
    for i in range(exp):
        total *= base
        total %= 1e10
    return total

        
total = 0
for i in range(1, 1001):
    total += findlasttendigits(i, i)

total %= 1e10
print(total)
