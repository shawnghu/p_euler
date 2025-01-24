import mpmath
import pdb
# mpmath.dps = 100 !!this line doesn't work, can you believe that?
mpmath.mp.dps = 100

a = mpmath.mpf(414213568004.0)
b = mpmath.mpf(585786445590.0)
c = a * (a - 1)
d = mpmath.fmul(b, b - 1)
e = b * (b - 1)
f = mpmath.fmul(b, b - 1, dps=28)
g = mpmath.fmul(b, b - 1, dps=50)
pdb.set_trace()


print(c)
print(d)
