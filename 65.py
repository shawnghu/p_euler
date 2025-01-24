import mpmath

sequence = [1 if x % 3 != 1 else (x // 3 + 1) * 2 for x in range(100)]
#print(sequence)

def compute_partial(n):
    denominator = mpmath.mpf(sequence[n])
    numerator = mpmath.mpf(1)
    for i in range(n - 1, -1, -1):
        numerator = sequence[i] * denominator + numerator
        numerator, denominator = denominator, numerator
    return numerator, denominator

mpmath.dps = 100
num, den = (compute_partial(98))
num += 2 * den
total = 0
for char in (mpmath.nstr(num, 60)):
    if char == '.':
        continue
    total += int(char)
print(total)


