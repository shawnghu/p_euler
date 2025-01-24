import math
fractions = []
for denom in range(1, 1000000):
    for numer in range(math.floor(denom * 0.42857), math.floor(denom * 0.42858) + 1):
        fractions.append((numer, denom))

fractions.sort(key=lambda x: x[0] / x[1])

idx = fractions.index((3, 7))

print(fractions[idx])
print(fractions[idx - 1])

