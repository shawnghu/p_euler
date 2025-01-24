import math
sqrt2 = math.sqrt(2)
for num in range(1000):
    for den in range(math.floor(sqrt2 * num) - 1, math.floor(sqrt2 * num) + 4):
        if num <= 1 or den <= 1:
            continue
        if num * (num - 1) / (den * (den - 1)) == 0.5:
            print(num, den)


