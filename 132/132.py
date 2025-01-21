from sympy.ntheory import factorint
'''

a = '1' * 100
a = int(a)
print(factorint(a))

b = '1' * 10
b = int(b)
print(factorint(b))

c = '1' * 100
c = int(c)
print(factorint(c))
'''

# observe: every factor of R(10) is a factor of R(10^2), since R(10) is itself a factor of R(10^2)
# in particular R(10^2) = R(10) * 1 (9 zeroes) 1 (9 zeroes) ... (9 times) 1, a 91 digit number slightly higher than 10^90
# we just have to care about the factors of that number, which apparently include 101, 251, 3541, 5051
# call that number C(10^2)
# now, observe: R(10^10) = R(10^1) * C(10^2) * C(10^3) * ... * C(10^10)
# formulaically, C(10^k) consists of a 1, 10^k-1 zeroes, repeated 9 times, and a 1 at the end, and is a 9 * (10^k - 1) + 1 digit number
# since we only need the first forty prime factors, i guess we probably only need five factors of each of these numbers

# "scientifically", the first question is: why does 101 divide C(10^2)?

# another approach, use some general properties of modular arithmetic to invert the problem
# R(k) * 9  + 1 = 10^k
# so if a prime p divides R(k), then 10^k is going to be equivalent to 1 mod p?
# well more importantly p divides R(k) IFF 10^k is equivalent to 1 mod 9p

# loose check
print(10 ** 10 % (9 * 11))
print(10 ** 10 % (9 * 41))
print(10 ** 10 % (9 * 271))
print(10 ** 10 % (9 * 9091))

# this one again shouldn't be that hard, so use crappy prime checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_factor_r10to9(p):
    q = 10
    for x in range(9):
        q = q ** 10 % (9 * p)
    return q == 1

prime_factors = []
potential_factor = 5
while True:
    if is_prime(potential_factor):
        if check_factor_r10to9(potential_factor):
            prime_factors.append(potential_factor)
        if len(prime_factors) == 40:
            break
    potential_factor += 2
print(sum(prime_factors))