import mpmath

mpmath.dps = 26
a = mpmath.mpf(3 ** 13)
b = mpmath.mpf(((3 ** 26 - 1) / 2))
c = mpmath.mpf(((3 ** 26 + 1) / 2))

d = mpmath.sqrt(a ** 2 + b ** 2)
print(d)
print(mpmath.isint(d))
print(d == c)
