# this one i think relies on a trick of modular arithmetic
import mpmath

mpmath.mp.dps = 1000

print(mpmath.mp.mpf(1) / 101)
print(mpmath.mp.mpf(1) / 14)